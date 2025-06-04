import sqlite3
from typing import List, Optional, Dict, Any


class TranscriptDatabase:
    def __init__(self, db_name: str = "transcript_system.db"):
        self.db_name = db_name
        self.create_tables()

    def get_connection(self):
        """Get database connection with foreign keys enabled"""
        conn = sqlite3.connect(self.db_name)
        conn.execute("PRAGMA foreign_keys = 1")
        return conn

    def create_tables(self):
        """Create all necessary tables for the transcript system"""
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

        # Create Course Names table (stores course codes and names)
        c.execute("""CREATE TABLE IF NOT EXISTS course_names (
            course_code TEXT PRIMARY KEY,
            course_name TEXT NOT NULL,
            dept_id TEXT,
            FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
        )""")

        # Create Curriculum Courses table (courses in each curriculum version)
        c.execute("""CREATE TABLE IF NOT EXISTS curriculum_courses (
            curriculum_id INTEGER,
            course_code TEXT,
            metu_credits TEXT NOT NULL,  -- Format: "5(4-2)" 
            ects_credits REAL NOT NULL,
            semester_suggested INTEGER DEFAULT 1,
            is_required BOOLEAN DEFAULT TRUE,
            PRIMARY KEY (curriculum_id, course_code),
            FOREIGN KEY (curriculum_id) REFERENCES curriculum_versions(curriculum_id),
            FOREIGN KEY (course_code) REFERENCES course_names(course_code)
        )""")

        # Create Prerequisites table
        c.execute("""CREATE TABLE IF NOT EXISTS prerequisites (
            curriculum_id INTEGER,
            course_code TEXT,
            prerequisite_code TEXT,
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
            status TEXT DEFAULT 'ACTIVE',
            FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
            FOREIGN KEY (curriculum_id) REFERENCES curriculum_versions(curriculum_id)
        )""")

        # Create Student Enrollments table (courses taken by students)
        c.execute("""CREATE TABLE IF NOT EXISTS student_enrollments (
            enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            course_code TEXT NOT NULL,
            semester TEXT NOT NULL,  -- Format: "2023-Fall" or "2024-Spring"
            grade TEXT,  -- AA, BA, BB, CB, CC, DC, DD, FF, EX, etc.
            attempt_number INTEGER DEFAULT 1,
            enrollment_date TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (course_code) REFERENCES course_names(course_code)
        )""")

        conn.commit()
        conn.close()

    def add_department(self, dept_id: str, dept_name: str) -> bool:
        """Add a new department"""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("INSERT INTO departments (dept_id, dept_name) VALUES (?, ?)",
                      (dept_id, dept_name))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            if conn:
                conn.close()

    def add_curriculum_version(self, dept_id: str, version_number: int,
                              version_name: str = None, effective_date: str = None) -> int:
        """Add a new curriculum version and return its ID"""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            
            # First check if this combination already exists
            c.execute("""SELECT curriculum_id FROM curriculum_versions 
                         WHERE dept_id = ? AND version_number = ?""", 
                     (dept_id, version_number))
            existing = c.fetchone()
            if existing:
                return existing[0]  # Return existing ID instead of creating duplicate
            
            # Insert new curriculum version if it doesn't exist
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
            print(f"Database error in add_curriculum_version: {e}")
            return -1
        finally:
            if conn:
                conn.close()
    
    def add_course_name(self, course_code: str, course_name: str, dept_id: str = None):
        """Add a course name to the database"""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("INSERT INTO course_names (course_code, course_name, dept_id) VALUES (?, ?, ?)",
                      (course_code, course_name, dept_id))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            if conn:
                conn.close()
    
    def add_curriculum_course(self, curriculum_id: int, course_code: str, 
                             metu_credits: str, ects_credits: float, 
                             is_required: bool = True, semester_suggested: int = 1):
        """Adds a course with its details to a specific curriculum version."""
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("""INSERT OR IGNORE INTO curriculum_courses
                     (curriculum_id, course_code, metu_credits, ects_credits, is_required, semester_suggested)
                     VALUES (?, ?, ?, ?, ?, ?)""",
                  (curriculum_id, course_code, metu_credits, ects_credits, is_required, semester_suggested))
            conn.commit()
            # print(f"Added course {course_code} to curriculum {curriculum_id}")
            return True
        except sqlite3.IntegrityError:
            # This can happen if the course_code + curriculum_id PK already exists
            # print(f"Warning: Course {course_code} likely already in curriculum {curriculum_id} or other integrity error.")
            return False
        finally:
            if conn:
                conn.close()


    def parse_curriculum_csv(self, csv_file_path: str, curriculum_id: int):
        """Parse curriculum CSV file and add courses to the curriculum"""
        conn = self.get_connection()
        c = conn.cursor()

        with open(csv_file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                # Remove inline comments
                if '#' in line:
                    parts = line.split('#', 1)
                    data_part = parts[0].strip()
                    comment_part = parts[1].strip() if len(parts) > 1 else ""
                else:
                    data_part = line
                    comment_part = ""

                if not data_part:
                    continue

                # Parse the CSV line
                try:
                    fields = [field.strip() for field in data_part.split(';')]
                    if len(fields) < 3:
                        print(f"Warning: Line {line_num} has insufficient fields")
                        continue

                    course_code = fields[0]
                    metu_credits = fields[1]
                    ects_credits = float(fields[2])
                    prerequisites = fields[3] if len(fields) > 3 and fields[3] else ""

                    # Extract course name from comment if available
                    course_name = ""
                    if comment_part:
                        # Format is usually "COURSE_CODE COURSE_NAME"
                        comment_parts = comment_part.split(' ', 1)
                        if len(comment_parts) > 1:
                            course_name = comment_parts[1]

                    # Add course name if not exists
                    if course_name:
                        c.execute("""INSERT OR IGNORE INTO course_names 
                                   (course_code, course_name) VALUES (?, ?)""",
                                  (course_code, course_name))

                    # Add curriculum course
                    c.execute("""INSERT INTO curriculum_courses 
                               (curriculum_id, course_code, metu_credits, ects_credits) 
                               VALUES (?, ?, ?, ?)""",
                              (curriculum_id, course_code, metu_credits, ects_credits))

                    # Add prerequisites
                    if prerequisites:
                        prereq_codes = [p.strip() for p in prerequisites.split(',')]
                        for prereq_code in prereq_codes:
                            if prereq_code:
                                c.execute("""INSERT INTO prerequisites 
                                           (curriculum_id, course_code, prerequisite_code) 
                                           VALUES (?, ?, ?)""",
                                          (curriculum_id, course_code, prereq_code))

                except ValueError as e:
                    print(f"Error parsing line {line_num}: {e}")
                    continue
                except Exception as e:
                    print(f"Unexpected error on line {line_num}: {e}")
                    continue

        conn.commit()
        conn.close()

    def add_student(self, student_id: str, first_name: str, last_name: str,
                    dept_id: str, curriculum_id: int, enrollment_year: int = None) -> bool:
        """Add a new student"""
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
            return False
        finally:
            if conn:
                conn.close()

    def add_enrollment(self, student_id: str, course_code: str, semester: str,
                       grade: str, attempt_number: int = 1) -> bool:
        """Add a student enrollment/grade"""
        conn = None
        try:
            conn = self.get_connection()
            c = conn.cursor()
            c.execute("""INSERT INTO student_enrollments 
                        (student_id, course_code, semester, grade, attempt_number) 
                        VALUES (?, ?, ?, ?, ?)""",
                      (student_id, course_code, semester, grade, attempt_number))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            if conn:
                conn.close()

    def get_student_info(self, student_id: str) -> Optional[Dict[str, Any]]:
        """Get student information"""
        conn = self.get_connection()
        c = conn.cursor()
        c.execute("""SELECT s.student_id, s.first_name, s.last_name, s.dept_id, 
                           d.dept_name, s.curriculum_id, cv.version_number, cv.version_name
                    FROM students s
                    JOIN departments d ON s.dept_id = d.dept_id
                    JOIN curriculum_versions cv ON s.curriculum_id = cv.curriculum_id
                    WHERE s.student_id = ?""", (student_id,))

        row = c.fetchone()
        conn.close()

        if row:
            return {
                'student_id': row[0],
                'first_name': row[1],
                'last_name': row[2],
                'dept_id': row[3],
                'dept_name': row[4],
                'curriculum_id': row[5],
                'curriculum_version': row[6],
                'curriculum_name': row[7]
            }
        return None

    def get_student_enrollments(self, student_id: str) -> List[Dict[str, Any]]:
        """Get all enrollments for a student"""
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
                    ORDER BY se.semester, se.course_code""", (student_id,))

        rows = c.fetchall()
        conn.close()

        enrollments = []
        for row in rows:
            enrollments.append({
                'course_code': row[0],
                'course_name': row[1],
                'semester': row[2],
                'grade': row[3],
                'attempt_number': row[4],
                'metu_credits': row[5],
                'ects_credits': row[6]
            })

        return enrollments

    def get_students_by_department(self, dept_id: str) -> List[str]:
        """Get all student IDs in a department"""
        conn = self.get_connection()
        c = conn.cursor()
        c.execute("SELECT student_id FROM students WHERE dept_id = ?", (dept_id,))
        rows = c.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def get_all_students(self) -> List[str]:
        """Get all student IDs"""
        conn = self.get_connection()
        c = conn.cursor()
        c.execute("SELECT student_id FROM students")
        rows = c.fetchall()
        conn.close()
        return [row[0] for row in rows]

    def populate_sample_data(self):
        """Populate database with sample data as required"""
        print("Populating database with sample data...")

        # Add departments
        departments = [
            ("SNG", "Software Engineering"),
            ("CSE", "Computer Science & Engineering"),
            ("EEE", "Electrical & Electronics Engineering")
        ]

        for dept_id, dept_name in departments:
            self.add_department(dept_id, dept_name)
            print(f"Added department: {dept_name}")

        # Add curriculum versions for each department
        curriculum_ids = {}
        for dept_id, dept_name in departments:
            for version in range(1, 4):  # 3 versions each
                curriculum_id = self.add_curriculum_version(
                    dept_id, version, f"{dept_name} Curriculum v{version}",
                    f"202{version}-09-01"
                )
                curriculum_ids[f"{dept_id}_v{version}"] = curriculum_id
                print(f"Added curriculum version {version} for {dept_name}")

        # Sample course names
        sample_courses = [
            ("3570119", "CALCULUS WITH ANALYTIC GEOMETRY"),
            ("3580105", "GENERAL PHYSICS I"),
            ("3600107", "GENERAL CHEMISTRY"),
            ("3590101", "DEVELOPMENT OF READING AND WRITING SKILLS I"),
            ("3550100", "INTRODUCTION TO INFORMATION TECH. AND APPLICATIONS"),
            ("3890101", "INTRODUCTION TO SOFTWARE ENGINEERING & ORIENTATION"),
            ("3890111", "INTRODUCTION TO COMPUTER SCIENCE AND PROGRAMMING"),
            ("3890330", "SOFTWARE DESIGN"),
            ("3890201", "DATA STRUCTURES"),
            ("3890242", "ALGORITHMS")
        ]

        for course_code, course_name in sample_courses:
            self.add_course_name(course_code, course_name)

        # Add sample students (25 per department, distributed across curriculum versions)
        import random
        student_counter = 1
        grades = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF"]
        semesters = ["2023-Fall", "2023-Spring", "2024-Fall", "2024-Spring"]

        for dept_id, dept_name in departments:
            for i in range(25):  # 25 students per department
                student_id = f"{dept_id}{2020 + (i % 5)}{str(student_counter).zfill(3)}"
                first_name = f"Student{student_counter}"
                last_name = f"Surname{student_counter}"

                # Assign to curriculum versions (distribute evenly)
                version = (i % 3) + 1
                curriculum_id = curriculum_ids[f"{dept_id}_v{version}"]

                self.add_student(student_id, first_name, last_name, dept_id,
                                 curriculum_id, 2020 + (i % 5))

                # Add some random enrollments
                for _ in range(random.randint(5, 10)):
                    course_code = random.choice(sample_courses)[0]
                    semester = random.choice(semesters)
                    grade = random.choice(grades)
                    self.add_enrollment(student_id, course_code, semester, grade)

                student_counter += 1

        print(f"Added {student_counter - 1} students with sample enrollments")
        print("Sample data population completed!")

    

if __name__ == "__main__":
    # Initialize database
    db = TranscriptDatabase()

    # Populate with sample data
    db.populate_sample_data()

    # Test some queries
    print("\n=== Testing Database ===")

    # Get a sample student
    all_students = db.get_all_students()
    if all_students:
        sample_student = all_students[0]
        student_info = db.get_student_info(sample_student)
        print(f"\nSample student info: {student_info}")

        enrollments = db.get_student_enrollments(sample_student)
        print(f"Student has {len(enrollments)} enrollments")

        if enrollments:
            print("First few enrollments:")
            for enrollment in enrollments[:3]:
                print(f"  {enrollment}")

