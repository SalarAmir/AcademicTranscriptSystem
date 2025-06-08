import sqlite3
import os
from typing import List, Tuple, Optional, Dict, Any
import random
# NEW: Import the curriculum data from the separate file
from curriculum_data import SNG_CURRICULA_DATA

class TranscriptDatabase:
    """
    Manages the SQLite database for a university transcript system.
    Handles operations related to departments, curricula, courses, students,
    and enrollments.
    """

    def __init__(self, db_name: str = "transcript_system.db"):
        """
        Initializes the database connection and ensures tables are created.
        """
        self.db_name = db_name
        db_dir = os.path.dirname(db_name)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir, exist_ok=True)
        self.create_tables()

    def get_connection(self) -> sqlite3.Connection:
        """Establishes and returns a database connection with foreign keys enabled."""
        conn = sqlite3.connect(self.db_name)
        conn.execute("PRAGMA foreign_keys = 1")
        return conn

    def create_tables(self):
        """Creates all necessary tables for the transcript system if they don't already exist."""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            # Departments table
            c.execute("""CREATE TABLE IF NOT EXISTS departments (
                dept_id TEXT PRIMARY KEY, dept_name TEXT NOT NULL, created_date TEXT DEFAULT CURRENT_TIMESTAMP
            )""")
            # Curriculum Versions table
            c.execute("""CREATE TABLE IF NOT EXISTS curriculum_versions (
                curriculum_id INTEGER PRIMARY KEY AUTOINCREMENT, dept_id TEXT NOT NULL, version_number INTEGER NOT NULL,
                version_name TEXT, effective_date TEXT DEFAULT CURRENT_TIMESTAMP, is_active BOOLEAN DEFAULT TRUE,
                FOREIGN KEY (dept_id) REFERENCES departments(dept_id), UNIQUE(dept_id, version_number)
            )""")
            # Course Names table
            c.execute("""CREATE TABLE IF NOT EXISTS course_names (
                course_code TEXT PRIMARY KEY, course_name TEXT NOT NULL, dept_id TEXT,
                FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
            )""")
            # Curriculum Courses table
            c.execute("""CREATE TABLE IF NOT EXISTS curriculum_courses (
                curriculum_id INTEGER NOT NULL, course_code TEXT NOT NULL, metu_credits TEXT NOT NULL,
                ects_credits REAL NOT NULL, semester_suggested INTEGER DEFAULT 1, is_required BOOLEAN DEFAULT TRUE,
                PRIMARY KEY (curriculum_id, course_code),
                FOREIGN KEY (curriculum_id) REFERENCES curriculum_versions(curriculum_id),
                FOREIGN KEY (course_code) REFERENCES course_names(course_code)
            )""")
            # Prerequisites table
            c.execute("""CREATE TABLE IF NOT EXISTS prerequisites (
                curriculum_id INTEGER NOT NULL, course_code TEXT NOT NULL, prerequisite_code TEXT NOT NULL,
                PRIMARY KEY (curriculum_id, course_code, prerequisite_code),
                FOREIGN KEY (curriculum_id) REFERENCES curriculum_versions(curriculum_id),
                FOREIGN KEY (course_code) REFERENCES course_names(course_code),
                FOREIGN KEY (prerequisite_code) REFERENCES course_names(course_code)
            )""")
            # Students table
            c.execute("""CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL,
                dept_id TEXT NOT NULL, curriculum_id INTEGER NOT NULL, enrollment_year INTEGER, status TEXT DEFAULT 'ACTIVE',
                FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
                FOREIGN KEY (curriculum_id) REFERENCES curriculum_versions(curriculum_id)
            )""")
            # Student Enrollments table
            c.execute("""CREATE TABLE IF NOT EXISTS student_enrollments (
                enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT, student_id TEXT NOT NULL, course_code TEXT NOT NULL,
                semester TEXT NOT NULL, grade TEXT, attempt_number INTEGER DEFAULT 1, enrollment_date TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (student_id) REFERENCES students(student_id),
                FOREIGN KEY (course_code) REFERENCES course_names(course_code),
                UNIQUE(student_id, course_code, semester)
            )""")
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error during table creation: {e}")
        finally:
            if conn:
                conn.close()

    def add_department(self, dept_id: str, dept_name: str) -> bool:
        """Adds a new department, ignoring if it already exists."""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("INSERT OR IGNORE INTO departments (dept_id, dept_name) VALUES (?, ?)", (dept_id, dept_name))
            conn.commit()
            return c.rowcount > 0
        except sqlite3.Error as e: print(f"Database error in add_department for {dept_id}: {e}"); return False
        finally:
            if conn: conn.close()

    def add_curriculum_version(self, dept_id: str, version_number: int,
                               version_name: str = None, effective_date: str = None) -> Optional[int]:
        """Adds a new curriculum version, returning its ID. If it exists, returns the existing ID."""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("SELECT curriculum_id FROM curriculum_versions WHERE dept_id = ? AND version_number = ?", (dept_id, version_number))
            existing_row = c.fetchone()
            if existing_row: return existing_row[0]
            
            c.execute("""INSERT INTO curriculum_versions (dept_id, version_number, version_name, effective_date) 
                         VALUES (?, ?, ?, ?)""", (dept_id, version_number, version_name, effective_date))
            curriculum_id = c.lastrowid
            conn.commit()
            return curriculum_id
        except sqlite3.Error as e: print(f"Database error in add_curriculum_version: {e}"); return None
        finally:
            if conn: conn.close()

    def add_course_name(self, course_code: str, course_name: str, dept_id: Optional[str] = None) -> bool:
        """Adds a new course name, ignoring if it already exists."""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("INSERT OR IGNORE INTO course_names (course_code, course_name, dept_id) VALUES (?, ?, ?)",
                      (course_code, course_name, dept_id))
            conn.commit()
            return c.rowcount > 0
        except sqlite3.Error as e: print(f"Database error in add_course_name: {e}"); return False
        finally:
            if conn: conn.close()
    
    def add_course_to_curriculum(self, curriculum_id: int, course_code: str, 
                                 metu_credits: str, ects_credits: float, 
                                 is_required: bool = True, semester_suggested: int = 1) -> bool:
        """Adds a course to a curriculum, ignoring if it already exists."""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("""INSERT OR IGNORE INTO curriculum_courses
                         (curriculum_id, course_code, metu_credits, ects_credits, is_required, semester_suggested)
                         VALUES (?, ?, ?, ?, ?, ?)""",
                      (curriculum_id, course_code, metu_credits, ects_credits, is_required, semester_suggested))
            conn.commit()
            return c.rowcount > 0
        except sqlite3.Error as e: print(f"Database error in add_course_to_curriculum: {e}"); return False
        finally:
            if conn: conn.close()

    def add_prerequisite(self, curriculum_id: int, course_code: str, prereq_code: str) -> bool:
        """Adds a prerequisite relationship for a course within a specific curriculum."""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("""INSERT OR IGNORE INTO prerequisites
                         (curriculum_id, course_code, prerequisite_code)
                         VALUES (?, ?, ?)""",
                      (curriculum_id, course_code, prereq_code))
            conn.commit()
            return c.rowcount > 0
        except sqlite3.Error as e: print(f"Database error adding prerequisite: {e}"); return False
        finally:
            if conn: conn.close()

    def add_student(self, student_id: str, first_name: str, last_name: str,
                    dept_id: str, curriculum_id: int, enrollment_year: int = None) -> bool:
        """Adds a new student to the database."""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("""INSERT INTO students
                         (student_id, first_name, last_name, dept_id, curriculum_id, enrollment_year)
                         VALUES (?, ?, ?, ?, ?, ?)""",
                      (student_id, first_name, last_name, dept_id, curriculum_id, enrollment_year))
            conn.commit()
            return True
        except sqlite3.IntegrityError: return False
        except sqlite3.Error as e: print(f"Database error in add_student for {student_id}: {e}"); return False
        finally:
            if conn: conn.close()

    def add_enrollment(self, student_id: str, course_code: str, semester: str,
                       grade: str, attempt_number: int = 1) -> bool:
        """Adds a student's enrollment, ignoring if it's a duplicate for that semester."""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("""INSERT OR IGNORE INTO student_enrollments
                         (student_id, course_code, semester, grade, attempt_number)
                         VALUES (?, ?, ?, ?, ?)""",
                      (student_id, course_code, semester, grade, attempt_number))
            conn.commit()
            return c.rowcount > 0
        except sqlite3.Error as e: print(f"Database error in add_enrollment for {student_id}, {course_code}: {e}"); return False
        finally:
            if conn: conn.close()

    def get_student_info(self, student_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves detailed information about a specific student."""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("""SELECT s.student_id, s.first_name, s.last_name, s.dept_id,
                               d.dept_name, s.curriculum_id, cv.version_number, cv.version_name
                         FROM students s
                         JOIN departments d ON s.dept_id = d.dept_id
                         JOIN curriculum_versions cv ON s.curriculum_id = cv.curriculum_id
                         WHERE s.student_id = ?""", (student_id,))
            row = c.fetchone()
            if row: return {'student_id': row[0], 'first_name': row[1], 'last_name': row[2],'dept_id': row[3], 'dept_name': row[4], 'curriculum_id': row[5],'curriculum_version': row[6], 'curriculum_name': row[7]}
            return None
        except sqlite3.Error as e: print(f"Database error in get_student_info for {student_id}: {e}"); return None
        finally:
            if conn: conn.close()

    def get_student_enrollments(self, student_id: str) -> List[Dict[str, Any]]:
        """Retrieves all course enrollments for a given student."""
        conn = None
        enrollments = []
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("""SELECT se.course_code, cn.course_name, se.semester, se.grade,
                               se.attempt_number, cc.metu_credits, cc.ects_credits
                         FROM student_enrollments se
                         JOIN course_names cn ON se.course_code = cn.course_code
                         LEFT JOIN students s ON se.student_id = s.student_id
                         LEFT JOIN curriculum_courses cc ON (s.curriculum_id = cc.curriculum_id AND se.course_code = cc.course_code)
                         WHERE se.student_id = ?
                         ORDER BY se.semester, cn.course_name, se.attempt_number""", (student_id,))
            rows = c.fetchall()
            for row in rows: enrollments.append({'course_code': row[0], 'course_name': row[1], 'semester': row[2], 'grade': row[3], 'attempt_number': row[4], 'metu_credits': row[5], 'ects_credits': row[6]})
            return enrollments
        except sqlite3.Error as e: print(f"Database error in get_student_enrollments for {student_id}: {e}"); return []
        finally:
            if conn: conn.close()

    def get_students_by_department(self, dept_id: str) -> List[str]:
        """Retrieves a list of student IDs for a given department."""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("SELECT student_id FROM students WHERE dept_id = ?", (dept_id,))
            rows = c.fetchall()
            return [row[0] for row in rows]
        except sqlite3.Error as e: print(f"Database error in get_students_by_department: {e}"); return []
        finally:
            if conn: conn.close()

    def get_all_students(self) -> List[str]:
        """Retrieves a list of all student IDs in the database."""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("SELECT student_id FROM students")
            rows = c.fetchall()
            return [row[0] for row in rows]
        except sqlite3.Error as e: print(f"Database error in get_all_students: {e}"); return []
        finally:
            if conn: conn.close()

    def populate_sample_data(self):
        """
        Populates the database using the embedded SNG curriculum data.
        """
        print("--- Starting Sample Data Population ---")
        
        # 1. Add Departments
        departments_data = [("SNG", "Software Engineering"), ("CSE", "Computer Science & Engineering"), ("EEE", "Electrical & Electronics Engineering")]
        print("1. Adding departments...")
        for dept_id, dept_name in departments_data:
            self.add_department(dept_id, dept_name)
        print("   Departments processed.")

        # 2. Populate SNG Curricula from the imported data
        sng_curriculum_ids = []
        print("\n2. Populating SNG curriculum from embedded data...")
        # The SNG_CURRICULA_DATA dictionary is now imported from curriculum_data.py
        for version_num, courses in SNG_CURRICULA_DATA.items():
            print(f"  Processing version {version_num}...")
            version_name = f"SNG Curriculum v{version_num} (Embedded)"
            curriculum_id = self.add_curriculum_version("SNG", version_num, version_name)
            
            if curriculum_id:
                courses_added_count = 0
                for course_data in courses:
                    self.add_course_name(course_data['code'], course_data['name'], "SNG")
                    if self.add_course_to_curriculum(curriculum_id, course_data['code'], course_data['metu'], course_data['ects'], semester_suggested=course_data['sem']):
                        courses_added_count += 1
                print(f"    -> Added {courses_added_count} courses to curriculum ID {curriculum_id}.")
                sng_curriculum_ids.append(curriculum_id)
            else:
                print(f"  Failed to create curriculum version {version_num}.")
        
        # 3. Add Students and Enrollments
        print("\n3. Adding students and their enrollments...")
        student_counter = 1
        grades = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF", "EX", "P", "NA"]
        first_names = ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Elif", "Cem", "Deniz", "Emir", "Selin"]
        last_names = ["Yilmaz", "Kaya", "Demir", "Şahin", "Çelik", "Yildiz", "Özdemir", "Arslan", "Koç", "Aydin"]

        for dept_id_loop, dept_name_loop in departments_data:
            print(f"  Populating 25 students for department: {dept_name_loop}")
            for _ in range(25):
                student_id = f"26{str(student_counter).zfill(5)}"
                first_name = random.choice(first_names)
                last_name = random.choice(last_names)
                enrollment_year = random.randint(2020, 2023)
                
                assigned_curriculum_id = None
                
                if dept_id_loop == "SNG" and sng_curriculum_ids:
                    assigned_curriculum_id = random.choice(sng_curriculum_ids)
                else:
                    assigned_curriculum_id = self.add_curriculum_version(dept_id_loop, 1, f"{dept_name_loop} Placeholder Curriculum")
                
                if assigned_curriculum_id is None:
                     student_counter += 1
                     continue

                if self.add_student(student_id, first_name, last_name, dept_id_loop, assigned_curriculum_id, enrollment_year):
                    conn_temp = self.get_connection()
                    c_temp = conn_temp.cursor()
                    # UPDATED QUERY: Fetch course_code and semester_suggested
                    c_temp.execute("SELECT course_code, semester_suggested FROM curriculum_courses WHERE curriculum_id = ?", 
                                   (assigned_curriculum_id,))
                    courses_in_curriculum = c_temp.fetchall() # List of (course_code, semester_suggested) tuples
                    conn_temp.close()

                    if courses_in_curriculum:
                        # NEW LOGIC: Enroll student in all courses according to their suggested semester
                        for course_code, semester_num in courses_in_curriculum:
                            # --- LOGIC TO MAP SEMESTER NUMBER TO ACADEMIC YEAR AND SEASON ---
                            year_offset = (semester_num - 1) // 2
                            is_spring = (semester_num % 2 == 0)
                            
                            enrollment_semester_year = enrollment_year + year_offset
                            enrollment_season = "Spring" if is_spring else "Fall"

                            semester_to_enroll = f"{enrollment_semester_year}-{enrollment_season}"
                            # --- END OF SEMESTER MAPPING LOGIC ---
                            
                            self.add_enrollment(student_id, course_code, semester_to_enroll, random.choice(grades))
                
                student_counter += 1
        
        print(f"\nProcessed {student_counter - 1} student profiles.")
        print("--- Sample Data Population Completed ---")


if __name__ == "__main__":
    db_file_name = "transcript_system.db"
    
    if os.path.exists(db_file_name):
        print(f"Removing existing database: {db_file_name} for a fresh run.")
        os.remove(db_file_name)
            
    db = TranscriptDatabase(db_name=db_file_name)
    db.populate_sample_data()

    print("\n=== Database Test Queries ===")
    all_students = db.get_all_students()
    print(f"Total students found in DB: {len(all_students)}")

    if all_students:
        test_student_ids = [s_id for s_id in all_students if s_id.startswith("26000")][:5]

        for student_id_to_test in test_student_ids:
            print(f"\n--- Fetching info for sample student: {student_id_to_test} ---")
            student_info = db.get_student_info(student_id_to_test)
            print(f"Student Info: {student_info}")

            if student_info:
                enrollments = db.get_student_enrollments(student_id_to_test)
                print(f"Student {student_id_to_test} has {len(enrollments)} enrollments.")
                if enrollments:
                    print("First few enrollments (max 3):")
                    for enrollment in enrollments[:3]:
                        print(f"  {enrollment}")
                else:
                    print("  No enrollments found for this student.")
            else:
                print(f"Could not retrieve info for student: {student_id_to_test}")
    else:
        print("No students found in the database to test queries.")
