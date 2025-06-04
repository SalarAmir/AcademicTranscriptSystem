import sqlite3
import csv
import os
from typing import List, Tuple, Optional, Dict, Any
import random # Moved import to the top

class TranscriptDatabase:
    def __init__(self, db_name: str = "transcript_system.db"):
        self.db_name = db_name
        # Ensure the directory for the DB exists if db_name includes a path
        db_dir = os.path.dirname(db_name)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir, exist_ok=True)
        self.create_tables()

    def get_connection(self) -> sqlite3.Connection:
        """Get database connection with foreign keys enabled"""
        conn = sqlite3.connect(self.db_name)
        conn.execute("PRAGMA foreign_keys = 1")
        return conn

    def create_tables(self):
        """Create all necessary tables for the transcript system"""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()

            # Create Departments table
            c.execute("""CREATE TABLE IF NOT EXISTS departments (
                dept_id TEXT PRIMARY KEY,
                dept_name TEXT NOT NULL,
                created_date TEXT DEFAULT CURRENT_TIMESTAMP
            )""")

            # Create Curriculum Versions table
            c.execute("""CREATE TABLE IF NOT EXISTS curriculum_versions (
                curriculum_id INTEGER PRIMARY KEY AUTOINCREMENT,
                dept_id TEXT NOT NULL,
                version_number INTEGER NOT NULL,
                version_name TEXT,
                effective_date TEXT DEFAULT CURRENT_TIMESTAMP,
                is_active BOOLEAN DEFAULT TRUE,
                FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
                UNIQUE(dept_id, version_number)
            )""")

            # Create Course Names table
            c.execute("""CREATE TABLE IF NOT EXISTS course_names (
                course_code TEXT PRIMARY KEY,
                course_name TEXT NOT NULL,
                dept_id TEXT, /* Optional: can indicate the primary dept offering the course */
                FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
            )""")

            # Create Curriculum Courses table
            c.execute("""CREATE TABLE IF NOT EXISTS curriculum_courses (
                curriculum_id INTEGER NOT NULL,
                course_code TEXT NOT NULL,
                metu_credits TEXT NOT NULL,  /* Format: "5(4-2)" */
                ects_credits REAL NOT NULL,
                semester_suggested INTEGER DEFAULT 1,
                is_required BOOLEAN DEFAULT TRUE,
                PRIMARY KEY (curriculum_id, course_code),
                FOREIGN KEY (curriculum_id) REFERENCES curriculum_versions(curriculum_id),
                FOREIGN KEY (course_code) REFERENCES course_names(course_code)
            )""")

            # Create Prerequisites table
            c.execute("""CREATE TABLE IF NOT EXISTS prerequisites (
                curriculum_id INTEGER NOT NULL,
                course_code TEXT NOT NULL,
                prerequisite_code TEXT NOT NULL,
                PRIMARY KEY (curriculum_id, course_code, prerequisite_code),
                FOREIGN KEY (curriculum_id) REFERENCES curriculum_versions(curriculum_id),
                FOREIGN KEY (course_code) REFERENCES course_names(course_code),
                FOREIGN KEY (prerequisite_code) REFERENCES course_names(course_code)
            )""")

            # Create Students table
            c.execute("""CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                dept_id TEXT NOT NULL,
                curriculum_id INTEGER NOT NULL,
                enrollment_year INTEGER,
                status TEXT DEFAULT 'ACTIVE', /* e.g., ACTIVE, GRADUATED, INACTIVE */
                FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
                FOREIGN KEY (curriculum_id) REFERENCES curriculum_versions(curriculum_id)
            )""")

            # Create Student Enrollments table
            # Added UNIQUE constraint for (student_id, course_code, semester)
            c.execute("""CREATE TABLE IF NOT EXISTS student_enrollments (
                enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                course_code TEXT NOT NULL,
                semester TEXT NOT NULL,  /* Format: "YYYY-Season", e.g., "2023-Fall" */
                grade TEXT,  /* AA, BA, BB, etc. */
                attempt_number INTEGER DEFAULT 1,
                enrollment_date TEXT DEFAULT CURRENT_TIMESTAMP,
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
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("INSERT OR IGNORE INTO departments (dept_id, dept_name) VALUES (?, ?)", (dept_id, dept_name))
            conn.commit()
            return c.rowcount > 0 # True if a row was inserted/ignored (effectively exists)
        except sqlite3.Error as e:
            print(f"Database error in add_department for {dept_id}: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def add_curriculum_version(self, dept_id: str, version_number: int,
                               version_name: str = None, effective_date: str = None) -> Optional[int]:
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("SELECT curriculum_id FROM curriculum_versions WHERE dept_id = ? AND version_number = ?", (dept_id, version_number))
            existing_row = c.fetchone()
            if existing_row:
                return existing_row[0]

            if effective_date:
                c.execute("""INSERT INTO curriculum_versions 
                             (dept_id, version_number, version_name, effective_date) 
                             VALUES (?, ?, ?, ?)""",
                          (dept_id, version_number, version_name, effective_date))
            else:
                c.execute("""INSERT INTO curriculum_versions 
                             (dept_id, version_number, version_name) 
                             VALUES (?, ?, ?)""",
                          (dept_id, version_number, version_name))
            curriculum_id = c.lastrowid
            conn.commit()
            return curriculum_id
        except sqlite3.Error as e:
            print(f"Database error in add_curriculum_version for D:{dept_id} V:{version_number}: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def add_course_name(self, course_code: str, course_name: str, dept_id: Optional[str] = None) -> bool:
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("INSERT OR IGNORE INTO course_names (course_code, course_name, dept_id) VALUES (?, ?, ?)",
                      (course_code, course_name, dept_id))
            conn.commit()
            return c.rowcount > 0
        except sqlite3.Error as e:
            print(f"Database error in add_course_name for {course_code}: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def add_course_to_curriculum(self, curriculum_id: int, course_code: str, 
                                 metu_credits: str, ects_credits: float, 
                                 is_required: bool = True, semester_suggested: int = 1) -> bool:
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
        except sqlite3.Error as e:
            print(f"Database error in add_course_to_curriculum for C:{course_code} in CurID:{curriculum_id}: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def parse_curriculum_csv(self, csv_file_path: str, curriculum_id: int):
        """Parse curriculum CSV file and add courses to the curriculum.
           Assumes CSV format: course_code;metu_credits;ects_credits;prerequisites_str # course_name
        """
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor() # Use a single cursor for the transaction
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue

                    comment_part = ""
                    if '#' in line:
                        parts = line.split('#', 1)
                        data_part = parts[0].strip()
                        if len(parts) > 1: comment_part = parts[1].strip()
                    else:
                        data_part = line
                    
                    if not data_part: continue

                    try:
                        fields = [field.strip() for field in data_part.split(';')]
                        if len(fields) < 3:
                            print(f"Warning (CSV Line {line_num}): Insufficient fields in '{data_part}'. Skipping.")
                            continue

                        course_code_csv = fields[0]
                        metu_credits_csv = fields[1]
                        ects_credits_csv = float(fields[2])
                        prerequisites_str = fields[3] if len(fields) > 3 and fields[3] else ""
                        
                        course_name_from_comment = ""
                        if comment_part:
                            first_space_index = comment_part.find(' ')
                            if first_space_index != -1 and comment_part[:first_space_index] == course_code_csv:
                                course_name_from_comment = comment_part[first_space_index+1:].strip()
                            else: course_name_from_comment = comment_part # Assume comment is just the name

                        if course_name_from_comment:
                            # This add_course_name uses its own connection, which is fine but less transactional.
                            # For a fully transactional parse, this logic could be inlined using 'c'.
                            self.add_course_name(course_code_csv, course_name_from_comment) 
                        
                        # Add course to curriculum using the main cursor 'c' for this method
                        c.execute("""INSERT OR IGNORE INTO curriculum_courses
                                     (curriculum_id, course_code, metu_credits, ects_credits) 
                                     VALUES (?, ?, ?, ?)""",
                                  (curriculum_id, course_code_csv, metu_credits_csv, ects_credits_csv))

                        if prerequisites_str:
                            prereq_codes = [p.strip() for p in prerequisites_str.split(',') if p.strip()]
                            for prereq_code in prereq_codes:
                                c.execute("""INSERT OR IGNORE INTO prerequisites 
                                             (curriculum_id, course_code, prerequisite_code) 
                                             VALUES (?, ?, ?)""",
                                          (curriculum_id, course_code_csv, prereq_code))
                    except ValueError as ve:
                        print(f"Warning (CSV Line {line_num}): Error parsing data '{data_part}'. {ve}. Skipping.")
                    except Exception as ex: # Catch more general exceptions per line
                        print(f"Warning (CSV Line {line_num}): Unexpected error processing '{data_part}'. {ex}. Skipping.")
            conn.commit() # Commit once after processing all lines
        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_file_path}")
        except sqlite3.Error as e:
            print(f"Database error in parse_curriculum_csv: {e}")
            if conn: conn.rollback()
        except Exception as e: # Catch other unexpected errors during file processing
            print(f"An unexpected error occurred in parse_curriculum_csv: {e}")
        finally:
            if conn:
                conn.close()

    def add_student(self, student_id: str, first_name: str, last_name: str,
                    dept_id: str, curriculum_id: int, enrollment_year: Optional[int] = None) -> bool:
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
        except sqlite3.IntegrityError:
            return False # Student ID (PK) likely already exists
        except sqlite3.Error as e:
            print(f"Database error in add_student for {student_id}: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def add_enrollment(self, student_id: str, course_code: str, semester: str,
                       grade: str, attempt_number: int = 1) -> bool:
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            # Using INSERT OR IGNORE due to UNIQUE constraint on (student_id, course_code, semester)
            c.execute("""INSERT OR IGNORE INTO student_enrollments 
                         (student_id, course_code, semester, grade, attempt_number) 
                         VALUES (?, ?, ?, ?, ?)""",
                      (student_id, course_code, semester, grade, attempt_number))
            conn.commit()
            return c.rowcount > 0 # True if a row was inserted (not ignored)
        except sqlite3.Error as e:
            print(f"Database error in add_enrollment for S:{student_id} C:{course_code} Sem:{semester}: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def get_student_info(self, student_id: str) -> Optional[Dict[str, Any]]:
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
            if row:
                return {
                    'student_id': row[0], 'first_name': row[1], 'last_name': row[2],
                    'dept_id': row[3], 'dept_name': row[4], 'curriculum_id': row[5],
                    'curriculum_version': row[6], 'curriculum_name': row[7]
                }
            return None
        except sqlite3.Error as e:
            print(f"Database error in get_student_info for {student_id}: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def get_student_enrollments(self, student_id: str) -> List[Dict[str, Any]]:
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
                         LEFT JOIN curriculum_courses cc ON (s.curriculum_id = cc.curriculum_id 
                                                           AND se.course_code = cc.course_code)
                         WHERE se.student_id = ?
                         ORDER BY se.semester, cn.course_name, se.attempt_number""", (student_id,))
            rows = c.fetchall()
            for row in rows:
                enrollments.append({
                    'course_code': row[0], 'course_name': row[1], 'semester': row[2],
                    'grade': row[3], 'attempt_number': row[4],
                    'metu_credits': row[5], 'ects_credits': row[6]
                })
            return enrollments
        except sqlite3.Error as e:
            print(f"Database error in get_student_enrollments for {student_id}: {e}")
            return []
        finally:
            if conn:
                conn.close()

    def get_students_by_department(self, dept_id: str) -> List[str]:
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("SELECT student_id FROM students WHERE dept_id = ?", (dept_id,))
            rows = c.fetchall()
            return [row[0] for row in rows]
        except sqlite3.Error as e:
            print(f"Database error in get_students_by_department for {dept_id}: {e}")
            return []
        finally:
            if conn:
                conn.close()

    def get_all_students(self) -> List[str]:
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("SELECT student_id FROM students")
            rows = c.fetchall()
            return [row[0] for row in rows]
        except sqlite3.Error as e:
            print(f"Database error in get_all_students: {e}")
            return []
        finally:
            if conn:
                conn.close()

    def populate_sample_data(self):
        """Populate database with sample data as required"""
        print("Starting sample data population...")

        # 1. Add Departments
        departments_data = [
            ("SNG", "Software Engineering"),
            ("CSE", "Computer Science & Engineering"),
            ("EEE", "Electrical & Electronics Engineering")
        ]
        print("Adding departments...")
        for dept_id, dept_name in departments_data:
            if self.add_department(dept_id, dept_name):
                print(f"  Department added/exists: {dept_name}")
            else:
                print(f"  Failed to add department: {dept_name}")

        # 2. Add Curriculum Versions
        curriculum_ids = {} 
        print("Adding curriculum versions...")
        for dept_id, dept_name in departments_data:
            for version_num in range(1, 4):
                curr_name = f"{dept_name} Curriculum v{version_num}"
                eff_date = f"202{version_num}-09-01"
                curr_id = self.add_curriculum_version(dept_id, version_num, curr_name, eff_date)
                if curr_id is not None:
                    curriculum_ids[f"{dept_id}_v{version_num}"] = curr_id
                    # print(f"  Curriculum version added/found: {curr_name} (ID: {curr_id})")
                else:
                    print(f"  Failed to add/find curriculum version {version_num} for {dept_name}")
        print(f"  {len(curriculum_ids)} curriculum versions processed.")

        # 3. Add Sample Course Names
        sample_courses_data = [ # (code, name, metu_credits_str, ects_float, offering_dept_shortcode_or_general)
            ("MAT119", "CALCULUS I", "5(4-2)", 7.5, "GEN"),
            ("PHY101", "PHYSICS I", "4(3-2)", 6.5, "GEN"),
            ("CHM107", "GENERAL CHEMISTRY", "4(3-2)", 6.0, "GEN"),
            ("ENG101", "ACADEMIC ENGLISH I", "4(4-0)", 6.0, "ENG"),
            ("CSE100", "INTRODUCTION TO CSE", "0(2-0)", 1.0, "CSE"), # Example: was 3550100
            ("SNG101", "INTRODUCTION TO SNG", "0(2-0)", 1.0, "SNG"), # Example: was 3890101
            ("CSE111", "PROGRAMMING I", "4(3-2)", 4.0, "CSE"),       # Example: was 3890111
            ("SNG330", "SOFTWARE DESIGN", "3(3-0)", 5.0, "SNG"),
            ("CSE201", "DATA STRUCTURES", "4(3-2)", 6.0, "CSE"),     # Example: was 3890201
            ("CSE242", "ALGORITHMS", "3(3-0)", 5.0, "CSE"),          # Example: was 3890242
            ("EEE201", "CIRCUIT THEORY I", "4(3-2)", 6.5, "EEE"),
            ("EEE281", "ELECTRICAL CIRCUITS LAB", "2(0-4)", 3.0, "EEE")
        ]
        print("Adding sample course names...")
        for code, name, _, _, _ in sample_courses_data: # Only need code and name here
            self.add_course_name(code, name) # Dept_id for course_names is optional
        print(f"  {len(sample_courses_data)} course names processed.")

        # 4. Populate 'curriculum_courses'
        print("Populating 'curriculum_courses'...")
        for curriculum_key, current_curriculum_id in curriculum_ids.items():
            # print(f"  Processing curriculum: {curriculum_key} (ID: {current_curriculum_id})")
            # Add general courses to all curricula
            for code, name, m_credits, e_credits, offering_dept in sample_courses_data:
                if offering_dept == "GEN" or offering_dept == "ENG": # Add all GEN/ENG courses
                     self.add_course_to_curriculum(
                        current_curriculum_id, code, m_credits, e_credits,
                        is_required=random.choice([True,True,False]), semester_suggested=random.randint(1,2)
                    )
                # Add department-specific courses
                elif ("SNG" in curriculum_key and offering_dept == "SNG") or \
                     ("CSE" in curriculum_key and offering_dept == "CSE") or \
                     ("EEE" in curriculum_key and offering_dept == "EEE"):
                    self.add_course_to_curriculum(
                        current_curriculum_id, code, m_credits, e_credits, True, random.randint(1,8)
                    )
        print("'curriculum_courses' populated.")

        # 5. Add Students and their Enrollments
        print("Adding students and their enrollments...")
        student_counter = 1
        grades = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF", "EX", "P", "NA"]
        semesters = ["2021-Fall", "2022-Spring", "2022-Fall", "2023-Spring", "2023-Fall", "2024-Spring"]
        first_names = ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Elif", "Cem", "Deniz", "Emir", "Selin"]
        last_names = ["Yilmaz", "Kaya", "Demir", "Şahin", "Çelik", "Yildiz", "Özdemir", "Arslan", "Koç", "Aydin"]

        for dept_id_loop, dept_name_loop in departments_data:
            # print(f"  Populating students for department: {dept_name_loop}")
            for i in range(25):
                student_id = f"26{str(student_counter).zfill(5)}"
                first_name = random.choice(first_names)
                last_name = random.choice(last_names)
                version_num_for_student = (i % 3) + 1
                curriculum_key_for_student = f"{dept_id_loop}_v{version_num_for_student}"
                
                if curriculum_key_for_student not in curriculum_ids:
                    print(f"Error: Curriculum key '{curriculum_key_for_student}' not found. Skipping student {student_id}.")
                    student_counter += 1; continue
                
                assigned_curriculum_id = curriculum_ids[curriculum_key_for_student]
                enrollment_year_val = 2020 + (student_counter % 4) # Vary enrollment year

                if self.add_student(student_id, first_name, last_name, dept_id_loop, assigned_curriculum_id, enrollment_year_val):
                    conn_temp = self.get_connection()
                    c_temp = conn_temp.cursor()
                    c_temp.execute("SELECT course_code FROM curriculum_courses WHERE curriculum_id = ?", (assigned_curriculum_id,))
                    courses_in_curriculum = [row[0] for row in c_temp.fetchall()]
                    conn_temp.close()

                    if courses_in_curriculum:
                        num_enrollments = random.randint(max(1, len(courses_in_curriculum)//2), len(courses_in_curriculum))
                        courses_to_enroll_in = random.sample(courses_in_curriculum, num_enrollments)
                        
                        # Track courses enrolled in this semester to avoid duplicates for this student
                        enrolled_this_semester_map: Dict[str, List[str]] = {} 

                        for course_code_to_enroll in courses_to_enroll_in:
                            semester_to_enroll = random.choice(semesters)
                            
                            # Ensure not enrolling in the same course twice in the same semester for this student
                            if semester_to_enroll not in enrolled_this_semester_map:
                                enrolled_this_semester_map[semester_to_enroll] = []
                            
                            if course_code_to_enroll not in enrolled_this_semester_map[semester_to_enroll]:
                                grade_to_assign = random.choice(grades)
                                self.add_enrollment(student_id, course_code_to_enroll, semester_to_enroll, grade_to_assign)
                                enrolled_this_semester_map[semester_to_enroll].append(course_code_to_enroll)
                            # else: print(f"    Skipping duplicate enrollment for S:{student_id} C:{course_code_to_enroll} Sem:{semester_to_enroll}")

                student_counter += 1
        
        print(f"Processed {student_counter - 1} student profiles.")
        print("Sample data population completed!")

# Main execution block
if __name__ == "__main__":
    db_file_name = "transcript_system.db"
    
    if os.path.exists(db_file_name):
        print(f"Removing existing database: {db_file_name} for a fresh run.")
        os.remove(db_file_name)
            
    db = TranscriptDatabase(db_name=db_file_name) # This calls create_tables
    db.populate_sample_data()

    print("\n=== Database Test Queries ===")
    all_students = db.get_all_students()
    print(f"Total students found in DB: {len(all_students)}")

    if all_students:
        test_student_ids = [s_id for s_id in all_students if int(s_id[2:]) % 10 == 1][:5] # Test some students ending in 1
        if not test_student_ids: test_student_ids = all_students[:3] # Fallback

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

