import sqlite3
import os
from typing import List, Tuple, Optional, Dict, Any
import random
# NEW: Import the curriculum data from the separate file
from curriculum_data import SNG_CURRICULA_DATA, EEE_CURRICULA_DATA, CNG_CURRICULA_DATA
from grade_calculator import GradeCalculator

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
        self.grade_calculator = GradeCalculator()  # Initialize here instead of in populate_sample_data

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
            
    def get_course_prerequisites(self, curriculum_id: int, course_code: str) -> List[str]:
        """Retrieves a list of prerequisite course codes for a given course."""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("SELECT prerequisite_code FROM prerequisites WHERE curriculum_id = ? AND course_code = ?", (curriculum_id, course_code))
            rows = c.fetchall()
            return [row[0] for row in rows]
        except sqlite3.Error as e:
            print(f"Database error in get_course_prerequisites: {e}")
            return []
        finally:
            if conn:
                conn.close()

    def get_student_passed_courses(self, student_id: str) -> List[str]:
        """Retrieves a list of course codes for courses a student has passed."""
        enrollments = self.get_student_enrollments(student_id)
        if not enrollments:
            return []

        grade_calculator = GradeCalculator()
        passed_courses = []
        for enrollment in enrollments:
            if grade_calculator.is_passing_grade(enrollment['grade']):
                passed_courses.append(enrollment['course_code'])
        return passed_courses

    def add_enrollment_with_prereq_check(self, student_id: str, course_code: str, semester: str) -> Tuple[bool, str]:
        """
        Enrolls a student in a course after checking prerequisites.
        Returns a tuple of (success_boolean, message_string).
        """
        student_info = self.get_student_info(student_id)
        if not student_info:
            return False, f"Student {student_id} not found."

        curriculum_id = student_info['curriculum_id']
        prerequisites = self.get_course_prerequisites(curriculum_id, course_code)
        
        if not prerequisites:
            # No prerequisites, so enrollment is allowed
            self.add_enrollment(student_id, course_code, semester, 'NA') # Enroll with a neutral grade initially
            return True, f"Successfully enrolled {student_id} in {course_code} (no prerequisites)."

        passed_courses = self.get_student_passed_courses(student_id)
        
        missing_prereqs = [prereq for prereq in prerequisites if prereq not in passed_courses]

        if not missing_prereqs:
            self.add_enrollment(student_id, course_code, semester, 'NA')
            return True, f"Successfully enrolled {student_id} in {course_code}."
        else:
            return False, f"Failed to enroll {student_id} in {course_code}. Missing prerequisites: {', '.join(missing_prereqs)}"


        # In TranscriptDatabase class
    def are_prerequisites_satisfied(self, student_id: str, curriculum_id: int, course_code: str) -> Tuple[bool, List[str]]:
        """Check if student has passed all prerequisites for a course"""
        prerequisites = self.get_course_prerequisites(curriculum_id, course_code)
        if not prerequisites:
            return True, []  # No prerequisites
        
        passed_courses = self.get_student_passed_courses(student_id)
        missing = [p for p in prerequisites if p not in passed_courses]
        return (len(missing) == 0, missing)
    
    # In TranscriptDatabase class
    def retake_failed_courses(self, student_id: str, current_semester: str):
        """Enroll student in courses failed in ALL attempts (never passed)"""
        enrollments = self.get_student_enrollments(student_id)
        passed_courses = set(self.get_student_passed_courses(student_id))
        courses_to_retake = set()
        
        # Identify courses failed in all attempts (never passed)
        for e in enrollments:
            course_code = e['course_code']
            if course_code in passed_courses:
                continue  # Skip if passed in any attempt
            if not self.grade_calculator.is_passing_grade(e['grade']):
                courses_to_retake.add(course_code)
        
        # Enroll using enroll_student (handles prerequisites/attempts)
        for course_code in courses_to_retake:
            self.enroll_student(student_id, course_code, current_semester)

    # In TranscriptDatabase class
    def enroll_student(self, student_id: str, course_code: str, semester: str) -> Tuple[bool, str]:
        """Enroll student in course with prerequisite checks and retake logic"""
        # Step 1: Check if student has already passed the course
        passed_courses = self.get_student_passed_courses(student_id)
        if course_code in passed_courses:
            return False, f"Student has already passed {course_code} and cannot enroll again."

        # Step 2: Check suggested semester constraint
        student_info = self.get_student_info(student_id)
        if not student_info:
            return False, "Student not found"
        
        curriculum_id = student_info['curriculum_id']
        enrollment_year = student_info.get('enrollment_year')
        
        if enrollment_year:
            # Parse semester string (e.g., "2021-Fall")
            parts = semester.split('-')
            if len(parts) == 2:
                try:
                    current_year = int(parts[0])
                    term = parts[1]
                    # Calculate current semester number
                    year_diff = current_year - enrollment_year
                    term_value = 1 if term == 'Fall' else 2
                    current_semester_num = year_diff * 2 + term_value
                    
                    # Fetch suggested semester from curriculum
                    conn = self.get_connection()
                    cursor = conn.cursor()
                    cursor.execute(
                        "SELECT semester_suggested FROM curriculum_courses "
                        "WHERE curriculum_id=? AND course_code=?",
                        (curriculum_id, course_code)
                    )
                    row = cursor.fetchone()
                    conn.close()
                    
                    if row:
                        suggested_semester = row[0]
                        if current_semester_num < suggested_semester:
                            return False, (
                                f"Cannot take {course_code} in {semester} (semester #{current_semester_num}). "
                                f"Suggested semester: #{suggested_semester}."
                            )
                except ValueError:
                    pass  # Skip if semester format is invalid

        # Step 3: Check prerequisites
        prereq_ok, missing = self.are_prerequisites_satisfied(student_id, curriculum_id, course_code)
        if not prereq_ok:
            return False, f"Missing prerequisites: {', '.join(missing)}"
        
        # Proceed with enrollment
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT MAX(attempt_number) FROM student_enrollments "
            "WHERE student_id=? AND course_code=?",
            (student_id, course_code)
        )
        max_attempt = cursor.fetchone()[0] or 0
        conn.close()
        
        success = self.add_enrollment(
            student_id,
            course_code,
            semester,
            'NA',  # Temporary grade
            attempt_number=max_attempt + 1
        )
        return (True, "Enrollment successful") if success else (False, "Enrollment failed")
    
    def register_for_semester(self, student_id: str, semester: str, courses: List[str]):
        """Handle full semester registration with prerequisites and retakes"""
        conn = self.get_connection()
        try:
            conn.execute("BEGIN TRANSACTION")
            results = []
            
            # First retake any failed courses
            self.retake_failed_courses(student_id, semester)
            
            # Then process new course requests
            for course_code in courses:
                success, message = self.enroll_student(student_id, course_code, semester)
                results.append((course_code, success, message))
            
            conn.commit()
            return results
        except Exception as e:
            conn.rollback()
            print(f"Error in register_for_semester: {e}")
            return [(course, False, str(e)) for course in courses]
        finally:
            conn.close()
    def populate_sample_data(self):
        """
        Populates the database using all three curriculum datasets.
        """
        print("--- Starting Sample Data Population ---")

        # 1. Add Departments
        departments_data = [
            ("CNG", "Computer Engineering"),
            ("EEE", "Electrical & Electronics Engineering"),
            ("SNG", "Software Engineering"),
            ("MAT", "Mathematics"),
            ("GER", "German Language"),
            ("ME", "Mechanical Engineering"),
            ("ENG", "English"),
            ("HST", "History"),
        ]
        print("1. Adding departments...")
        for dept_id, dept_name in departments_data:
            self.add_department(dept_id, dept_name)
        print("   Departments processed.")

        curricula_datasets = {
            "CNG": CNG_CURRICULA_DATA,
            "EEE": EEE_CURRICULA_DATA,
            "SNG": SNG_CURRICULA_DATA
        }
        
        # 2. Pre-populate all course names to satisfy foreign key constraints
        print("\n2. Pre-populating all course names...")
        all_courses = set()
        
        # Add external prerequisites first
        external_prereqs = [
            {'code': '3570100', 'name': 'Pre-Calculus', 'dept_id': 'MAT'},
            {'code': '3660271', 'name': 'German Language and Culture I', 'dept_id': 'GER'},
            {'code': '3660272', 'name': 'German Language and Culture II', 'dept_id': 'GER'},
            {'code': '6040201', 'name': 'Advanced German I', 'dept_id': 'GER'},
            {'code': '6040202', 'name': 'Advanced German II', 'dept_id': 'GER'},
            {'code': '2360119', 'name': 'Calculus for Technical Programs', 'dept_id': 'MAT'},
            {'code': '2360117', 'name': 'Applied Calculus', 'dept_id': 'MAT'},
            {'code': '6390101', 'name': 'English for Academic Purposes I', 'dept_id': 'ENG'},
            {'code': '2402201', 'name': 'History of the Turkish Republic I', 'dept_id': 'HST'},
        ]
        for course_data in external_prereqs:
            all_courses.add((course_data['code'], course_data['name'], course_data['dept_id']))

        # Add courses from main curricula
        for dept_id, curriculum_data in curricula_datasets.items():
            for version_num, courses in curriculum_data.items():
                for course_data in courses:
                    all_courses.add((course_data['code'], course_data['name'], dept_id))
        
        for course_code, course_name, dept_id in all_courses:
            self.add_course_name(course_code, course_name, dept_id)
        print("   All unique course names have been added.")

        # 3. Populate curricula and prerequisites  
        # INDENTATION FIXED: This entire section should be indented under populate_sample_data
        all_curriculum_ids = {"CNG": [], "EEE": [], "SNG": []}
        print("\n3. Populating curricula and prerequisites...")
        for dept_id, curriculum_data in curricula_datasets.items():
            print(f"  Processing {dept_id} curricula...")
            for version_num, courses in curriculum_data.items():
                print(f"    Processing version {version_num}...")
                version_name = f"{dept_id} Curriculum v{version_num} (Embedded)"
                curriculum_id = self.add_curriculum_version(dept_id, version_num, version_name)

                if curriculum_id:
                    courses_added_count = 0
                    for course_data in courses:
                        if self.add_course_to_curriculum(
                                curriculum_id,
                                course_data['code'],
                                course_data['metu'],
                                course_data['ects'],
                                semester_suggested=course_data['sem']
                        ):
                            courses_added_count += 1
                        if course_data.get('prerequisites'):
                            for prereq_code in course_data['prerequisites']:
                                self.add_prerequisite(curriculum_id, course_data['code'], prereq_code)

                    print(f"      -> Added {courses_added_count} courses to curriculum ID {curriculum_id}.")
                    all_curriculum_ids[dept_id].append(curriculum_id)
                else:
                    print(f"    Failed to create curriculum version {version_num} for {dept_id}.")
        
        # 4. Add Students and Enrollments with improved academic progression
        # INDENTATION FIXED: This entire section should be indented under populate_sample_data
        print("\n4. Adding students and their enrollments...")
        student_counter = 1
        first_names = ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Elif", "Cem", "Deniz", "Emir", "Selin"]
        last_names = ["Yilmaz", "Kaya", "Demir", "Şahin", "Çelik", "Yildiz", "Özdemir", "Arslan", "Koç", "Aydin"]
        
        # Consistent semesters for academic progression
        semesters = [
            "2021-Fall", "2022-Spring", 
            "2022-Fall", "2023-Spring", 
            "2023-Fall", "2024-Spring", 
            "2024-Fall", "2025-Spring"
        ]
        
        for dept_id_loop, dept_name_loop in [("CNG", "Computer Engineering"), ("EEE", "Electrical & Electronics Engineering"), ("SNG", "Software Engineering")]:
            print(f"  Populating 25 students for department: {dept_name_loop}")
            for _ in range(25):
                student_id = f"26{str(student_counter).zfill(5)}"
                first_name = random.choice(first_names)
                last_name = random.choice(last_names)
                enrollment_year = random.randint(2020, 2023)
                
                assigned_curriculum_id = None
                
                if all_curriculum_ids[dept_id_loop]:
                    assigned_curriculum_id = random.choice(all_curriculum_ids[dept_id_loop])
                else:
                    assigned_curriculum_id = self.add_curriculum_version(dept_id_loop, 1, f"{dept_name_loop} Placeholder Curriculum")
                
                if assigned_curriculum_id is None:
                     student_counter += 1
                     continue

                if self.add_student(student_id, first_name, last_name, dept_id_loop, assigned_curriculum_id, enrollment_year):
                    conn_temp = self.get_connection()
                    c_temp = conn_temp.cursor()
                    # Fetch course_code, semester_suggested and metu_credits
                    c_temp.execute("SELECT course_code, semester_suggested, metu_credits FROM curriculum_courses WHERE curriculum_id = ?", 
                                   (assigned_curriculum_id,))
                    curriculum_courses = c_temp.fetchall()
                    conn_temp.close()

                    if curriculum_courses:
                        # Organize courses by suggested semester
                        courses_by_semester = {}
                        for course in curriculum_courses:
                            sem = course[1]  # semester_suggested
                            if sem not in courses_by_semester:
                                courses_by_semester[sem] = []
                            courses_by_semester[sem].append(course[0])  # course_code

                        # Simulate academic progression through semesters
                        for semester_num in range(1, min(7, len(semesters) + 1)):  # Up to 6 semesters or available semesters
                            # Map to actual semester string
                            actual_semester = semesters[semester_num - 1]
                            
                            # Get courses for this semester level
                            semester_courses = courses_by_semester.get(semester_num, [])
                            
                            # Register for semester with prerequisite checks
                            self.register_for_semester(
                                student_id,
                                actual_semester,
                                semester_courses
                            )
                            
                            # Generate random grades for current semester
                            enrollments = self.get_student_enrollments(student_id)
                            for enrollment in enrollments:
                                if enrollment['semester'] == actual_semester and enrollment['grade'] == 'NA':
                                    credit_hours = self.grade_calculator.extract_credit_hours(
                                        enrollment['metu_credits']
                                    )
                                    
                                    # Select appropriate grading system based on credit hours
                                    if credit_hours == 0:
                                        grades = ["S", "U"]  # Satisfactory/Unsatisfactory
                                    else:
                                        grades = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF"]
                                    
                                    # Update enrollment with grade
                                    conn = self.get_connection()
                                    cursor = conn.cursor()
                                    cursor.execute(
                                        "UPDATE student_enrollments SET grade=? "
                                        "WHERE student_id=? AND course_code=? AND semester=?",
                                        (random.choice(grades), student_id, enrollment['course_code'], actual_semester)
                                    )
                                    conn.commit()
                                    conn.close()
                
                student_counter += 1
        
        print(f"\nProcessed {student_counter - 1} student profiles.")
        print("--- Sample Data Population Completed ---")


    def create_sample_student(self, student_id: str, first_name: str, last_name: str, 
                         dept_id: str, curriculum_id: int, enrollment_year: int) -> bool:
        """Create a student with basic information"""
        return self.add_student(student_id, first_name, last_name, dept_id, curriculum_id, enrollment_year)

    def simulate_student_progression(self, student_id: str, semesters: List[str]):
        """Simulate a student's academic progression through multiple semesters"""
        student_info = self.get_student_info(student_id)
        if not student_info:
            return False
        
        conn_temp = self.get_connection()
        c_temp = conn_temp.cursor()
        c_temp.execute("SELECT course_code, semester_suggested, metu_credits FROM curriculum_courses WHERE curriculum_id = ?", 
                      (student_info['curriculum_id'],))
        curriculum_courses = c_temp.fetchall()
        conn_temp.close()

        if not curriculum_courses:
            return False
            
        # Organize courses by suggested semester
        courses_by_semester = {}
        for course in curriculum_courses:
            sem = course[1]  # semester_suggested
            if sem not in courses_by_semester:
                courses_by_semester[sem] = []
            courses_by_semester[sem].append(course[0])  # course_code

        # Process each semester
        for semester_num in range(1, min(len(courses_by_semester) + 1, len(semesters) + 1)):
            actual_semester = semesters[semester_num - 1]
            semester_courses = courses_by_semester.get(semester_num, [])
            
            # Register for semester
            self.register_for_semester(student_id, actual_semester, semester_courses)
            
            # Generate grades
            self.assign_random_grades_for_semester(student_id, actual_semester)
            
        return True
    
    def assign_random_grades_for_semester(self, student_id: str, semester: str):
        """Assign random grades to a student's courses for a specific semester"""
        enrollments = self.get_student_enrollments(student_id)
        for enrollment in enrollments:
            if enrollment['semester'] == semester and enrollment['grade'] == 'NA':
                credit_hours = self.grade_calculator.extract_credit_hours(enrollment['metu_credits'])
                
                # Select appropriate grade scale based on credit hours
                if credit_hours == 0:
                    grades = ["S", "U"]  # Pass/Fail
                else:
                    grades = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF"]
                
                # Weight grades to make passing more common than failing (optional)
                weights = [0.15, 0.15, 0.15, 0.15, 0.15, 0.1, 0.05, 0.1]  # 90% pass rate
                
                if len(grades) == 2:  # For pass/fail courses
                    grade = random.choice(grades)
                else:
                    grade = random.choices(grades, weights=weights)[0]
                
                self.update_grade(student_id, enrollment['course_code'], semester, grade)

    def update_grade(self, student_id: str, course_code: str, semester: str, new_grade: str) -> bool:
        """Update the grade for a specific enrollment"""
        conn = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE student_enrollments SET grade=? "
                "WHERE student_id=? AND course_code=? AND semester=?",
                (new_grade, student_id, course_code, semester)
            )
            conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Database error updating grade: {e}")
            return False
        finally:
            if conn:
                conn.close()

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
        
    print("\n=== Prerequisite Check Demonstration ===")
    test_student_id = "2600001"
    course_to_test = "3570120"  # Calculus for Functions of Several Variables
    prereq_for_course = "3570119" # Calculus with Analytic Geometry

    print(f"\nAttempting to enroll student {test_student_id} in {course_to_test} without prerequisite...")
    # First, let's remove any existing passing grades for the prerequisite to ensure the check fails
    conn = db.get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM student_enrollments WHERE student_id = ? AND course_code = ? AND grade IN ('AA', 'BA', 'BB', 'CB', 'CC', 'DC', 'DD', 'S', 'P', 'EX')", (test_student_id, prereq_for_course))
    conn.commit()
    conn.close()

    success, message = db.add_enrollment_with_prereq_check(test_student_id, course_to_test, "2025-Fall")
    print(f"Result: {message}")

    print(f"\nNow, let's add the prerequisite {prereq_for_course} with a passing grade...")
    db.add_enrollment(test_student_id, prereq_for_course, "2024-Spring", "CC")
    print(f"Enrollment record added for {prereq_for_course}.")
    
    print(f"\nAttempting to enroll student {test_student_id} in {course_to_test} again...")
    success, message = db.add_enrollment_with_prereq_check(test_student_id, course_to_test, "2025-Fall")
    print(f"Result: {message}")

    print("\n=== Grade Update Test ===")
    test_student_id = "2600001"
    test_course_code = "3570120"
    test_semester = "2025-Fall"
    new_grade = "BB"

    print(f"\nUpdating grade for student {test_student_id}, course {test_course_code}, semester {test_semester} to {new_grade}...")
    if db.update_grade(test_student_id, test_course_code, test_semester, new_grade):
        print("Grade updated successfully.")
    else:
        print("Failed to update grade.")
    
    # Verify the update
    print(f"\nFetching updated enrollment record for verification...")
    updated_enrollment = db.get_student_enrollments(test_student_id)
    for enrollment in updated_enrollment:
        if enrollment['course_code'] == test_course_code and enrollment['semester'] == test_semester:
            print(f"Updated Enrollment Record: {enrollment}")
            break