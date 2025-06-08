from database import TranscriptDatabase
import os

def main():
    """
    This script demonstrates how to populate a specific curriculum
    from a detailed CSV file.
    """
    DB_FILE = "transcript_system.db"
    
    # Define the department and the new curriculum version to be populated
    DEPT_ID = "SNG"
    CURRICULUM_VERSION = 2023 # Example version number
    CURRICULUM_NAME = "SNG Official Curriculum (from CSV)"
    
    # IMPORTANT: Make sure this path is correct for your file system
    CSV_PATH = "SNG_Complete_Curriculum.csv"

    # --- SCRIPT LOGIC ---
    
    # 1. Check if the CSV file exists before proceeding
    if not os.path.exists(CSV_PATH):
        print(f"Error: Cannot find the curriculum CSV file at '{os.path.abspath(CSV_PATH)}'")
        print("Please make sure the file exists and the path is correct.")
        return

    # 2. Connect to the database
    db = TranscriptDatabase(db_name=DB_FILE)
    print(f"Connected to database: {DB_FILE}")

    # 3. Create a new curriculum version for the SNG department
    #    The add_curriculum_version method will return the ID if it already exists.
    print(f"Adding/finding curriculum version '{CURRICULUM_NAME}' for department '{DEPT_ID}'...")
    curriculum_id = db.add_curriculum_version(
        dept_id=DEPT_ID,
        version_number=CURRICULUM_VERSION,
        version_name=CURRICULUM_NAME
    )

    if curriculum_id is None or curriculum_id < 0:
        print("Error: Could not create or find the curriculum version in the database. Aborting.")
        return
        
    print(f"Successfully retrieved curriculum ID: {curriculum_id}")

    # 4. Call the new method to populate this curriculum from the CSV
    db.populate_curriculum_from_csv(curriculum_id, CSV_PATH)

    print("\nProcess finished.")

    # ... (at the end of the main() function in populate_from_csv.py) ...

    # --- ADD THIS SECTION TO CREATE A TEST STUDENT ---
    print("\nCreating a test student for the new curriculum...")
    
    # 1. Define a test student ID
    test_student_id = "2699999"
    
    # 2. Add the student to the database, assigning them to the curriculum_id we just populated
    if db.add_student(
        student_id=test_student_id,
        first_name="Test",
        last_name="Student",
        dept_id=DEPT_ID,
        curriculum_id=curriculum_id
    ):
        print(f"  Successfully added test student with ID: {test_student_id}")
        
        # 3. Enroll the student in some courses from their new curriculum
        conn = db.get_connection()
        c = conn.cursor()
        c.execute("SELECT course_code FROM curriculum_courses WHERE curriculum_id = ? LIMIT 10", (curriculum_id,))
        courses_to_enroll = [row[0] for row in c.fetchall()]
        conn.close()

        print(f"  Enrolling test student in {len(courses_to_enroll)} courses...")
        if courses_to_enroll:
            db.add_enrollment(test_student_id, courses_to_enroll[0], "2023-Fall", "AA")
            db.add_enrollment(test_student_id, courses_to_enroll[1], "2023-Fall", "BA")
            db.add_enrollment(test_student_id, courses_to_enroll[2], "2024-Spring", "CB")
            db.add_enrollment(test_student_id, courses_to_enroll[3], "2024-Spring", "FF")
            db.add_enrollment(test_student_id, courses_to_enroll[4], "2024-Spring", "BB")
        print("  Enrollments added.")

    else:
        print(f"  Test student {test_student_id} may have already existed.")
    
    print("\nProcess finished. You can now generate a transcript for student 2699999.")

if __name__ == "__main__":
    # It's recommended to run this on a fresh database to avoid conflicts
    # with existing sample data if they share course codes.
    # You can run `database.py` first (which deletes and recreates the DB)
    # before running this script.
    main()