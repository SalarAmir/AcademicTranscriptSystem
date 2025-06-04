"""
Transcript Generator for METU NCC Transcript System
Main orchestrator that combines database operations with grade calculations
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from database import TranscriptDatabase # Assuming database.py is in the same directory or accessible
from grade_calculator import GradeCalculator, CourseGrade # Assuming grade_calculator.py is accessible
import os # os is not directly used in this version, but often kept for path manipulations if needed elsewhere
from datetime import datetime


@dataclass
class TranscriptData:
    """Complete transcript data for a student"""
    # Student Information
    student_id: str
    full_name: str
    first_name: str
    last_name: str
    department: str
    department_name: str
    curriculum_version: str
    curriculum_name: str

    # Academic Summary
    overall_cgpa: float
    total_credits_completed: float
    total_credits_passed: float
    academic_standing: str

    # Semester-by-semester data
    semester_summaries: Dict[str, Dict]  # semester -> summary data

    # All course grades (for detailed view)
    all_grades: List[CourseGrade] # This stores all attempts
    latest_grades: Dict[str, CourseGrade]  # course_code -> latest grade for that course

    # Metadata
    generation_date: str
    transcript_type: str = "Official Academic Transcript"


class TranscriptGenerator:
    """
    Main class for generating student transcripts
    Orchestrates database queries and grade calculations
    """

    def __init__(self, db_path: str = "transcript_system.db"):
        self.database = TranscriptDatabase(db_path)
        self.grade_calculator = GradeCalculator()

    def generate_student_transcript(self, student_id: str) -> Optional[TranscriptData]:
        """
        Generate complete transcript data for a single student
        """
        student_info = self.database.get_student_info(student_id)
        if not student_info:
            print(f"Error: Student {student_id} not found")
            return None

        enrollments = self.database.get_student_enrollments(student_id)
        if not enrollments:
            # It's valid for a student to have no enrollments yet.
            # A warning is good, but we should still produce a transcript (empty academic record).
            print(f"Warning: No enrollments found for student {student_id}. Transcript will have an empty academic record.")
            course_grades = [] # Ensure course_grades is an empty list
        else:
            course_grades = self.grade_calculator.process_course_grades(enrollments)

        # Calculate overall CGPA and totals
        # These methods in grade_calculator should handle empty course_grades gracefully (e.g., return 0s)
        cgpa, total_points, total_credits = self.grade_calculator.calculate_cgpa(course_grades)

        latest_grades = self.grade_calculator.get_latest_grades(course_grades)
        completion_status = self.grade_calculator.calculate_completion_status(course_grades)
        academic_standing = self.grade_calculator.get_academic_standing(cgpa)
        
        semester_grades = self.grade_calculator.group_grades_by_semester(course_grades)
        semester_summaries = self.grade_calculator.calculate_semester_summary(semester_grades)

        full_name = f"{student_info['first_name']} {student_info['last_name']}"

        transcript_data = TranscriptData(
            student_id=student_id,
            full_name=full_name,
            first_name=student_info['first_name'],
            last_name=student_info['last_name'],
            department=student_info['dept_id'],
            department_name=student_info['dept_name'],
            curriculum_version=f"Version {student_info['curriculum_version']}", # Consider if 'Version' prefix is always wanted
            curriculum_name=student_info.get('curriculum_name', ''), # .get is good for optional fields
            overall_cgpa=cgpa,
            total_credits_completed=completion_status['completed_credits'],
            total_credits_passed=completion_status['passed_credits'],
            academic_standing=academic_standing,
            semester_summaries=semester_summaries,
            all_grades=course_grades, # Storing all grades (including all attempts)
            latest_grades=latest_grades, # Storing only the latest grade for each course
            generation_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        return transcript_data

    def generate_department_transcripts(self, dept_id: str) -> List[TranscriptData]:
        """
        Generate transcript data for all students in a department.
        Returns a list of TranscriptData objects.
        """
        student_ids = self.database.get_students_by_department(dept_id)

        if not student_ids:
            print(f"No students found in department {dept_id}")
            return []

        print(f"Generating transcript data for {len(student_ids)} students in department {dept_id}")

        generated_data_list = []
        success_count = 0

        for student_id in student_ids:
            try:
                transcript_data = self.generate_student_transcript(student_id)
                if transcript_data:
                    generated_data_list.append(transcript_data)
                    success_count += 1
                # else: generate_student_transcript already prints an error or warning
            except Exception as e:
                print(f"Error generating transcript data for student {student_id}: {e}")

        print(f"Successfully generated data for {success_count} transcripts for department {dept_id}")
        return generated_data_list

    def generate_all_transcripts(self) -> List[TranscriptData]:
        """
        Generate transcript data for all students in the university.
        Returns a list of TranscriptData objects.
        """
        all_student_ids = self.database.get_all_students() # Renamed for clarity

        if not all_student_ids:
            print("No students found in database")
            return []

        print(f"Generating transcript data for {len(all_student_ids)} students")

        generated_data_list = []
        success_count = 0

        for student_id in all_student_ids:
            try:
                transcript_data = self.generate_student_transcript(student_id)
                if transcript_data:
                    generated_data_list.append(transcript_data)
                    success_count += 1
                # else: generate_student_transcript already prints an error or warning
            except Exception as e:
                print(f"Error generating transcript data for student {student_id}: {e}")

        print(f"Successfully generated data for {success_count} total transcripts")
        return generated_data_list

    def print_transcript_summary(self, transcript_data: TranscriptData):
        """
        Print a text summary of the transcript (for testing/debugging)
        """
        print(f"\n{'=' * 60}")
        print(f"OFFICIAL ACADEMIC TRANSCRIPT")
        print(f"{'=' * 60}")
        print(f"Student ID: {transcript_data.student_id}")
        print(f"Name: {transcript_data.full_name}")
        print(f"Department: {transcript_data.department_name}")
        print(f"Curriculum: {transcript_data.curriculum_version} ({transcript_data.curriculum_name})")
        print(f"Generated: {transcript_data.generation_date}")
        print(f"\nAcademic Summary:")
        print(f"  Cumulative GPA: {transcript_data.overall_cgpa:.2f}")
        print(f"  Credits Completed (GPA affecting): {transcript_data.total_credits_completed:.1f}") # Clarified meaning
        print(f"  Credits Passed (GPA affecting): {transcript_data.total_credits_passed:.1f}") # Clarified meaning
        print(f"  Academic Standing: {transcript_data.academic_standing}")

        print(f"\nSemester-by-Semester Record:")
        if transcript_data.semester_summaries:
            print(f"{'Semester':<15} {'Courses':<8} {'GPA':<6} {'CGPA':<6} {'Credits':<8}")
            print(f"{'-' * 50}")
            for semester in sorted(transcript_data.semester_summaries.keys()):
                summary = transcript_data.semester_summaries[semester]
                num_courses = len(summary['courses'])
                semester_gpa = summary['semester_gpa']
                cgpa_at_semester_end = summary['cumulative_gpa'] # This is CGPA *up to and including* this semester
                semester_credits = summary['semester_credits']
                print(f"{semester:<15} {num_courses:<8} {semester_gpa:<6.2f} {cgpa_at_semester_end:<6.2f} {semester_credits:<8.1f}")
        else:
            print("  No semester data available.")

        print(f"\nDetailed Course Record (Latest Attempts for GPA Courses):")
        if transcript_data.latest_grades:
            print(f"{'Course':<12} {'Title':<30} {'Semester':<12} {'Grade':<6} {'Credits':<8}")
            print(f"{'-' * 75}")
            for course_code, grade_info in sorted(transcript_data.latest_grades.items()): # Sort for consistent output
                # Ensure grade_info is a CourseGrade object as expected by GradeCalculator
                if isinstance(grade_info, CourseGrade):
                    course_title = grade_info.course_name[:28] + "..." if len(grade_info.course_name) > 30 else grade_info.course_name
                    print(
                        f"{course_code:<12} {course_title:<30} {grade_info.semester:<12} {grade_info.grade:<6} {grade_info.credit_hours:<8.1f}")
                else:
                    print(f"  Warning: Malformed grade_info for course {course_code}")
        else:
            print("  No course records available.")


    def get_transcript_statistics(self) -> Dict[str, Any]:
        """
        Get overall statistics about the transcript system
        """
        all_student_ids = self.database.get_all_students()

        stats = {
            'total_students': len(all_student_ids),
            'departments': {},      # dept_id -> {count, avg_cgpa, total_cgpa}
            'grade_distribution': {}, # grade_letter -> count
            'average_cgpa': 0.0
        }

        total_cgpa_sum_for_avg = 0.0 # Renamed for clarity
        valid_cgpa_students_count = 0 # Renamed for clarity

        for student_id in all_student_ids:
            try:
                transcript_data = self.generate_student_transcript(student_id)
                if transcript_data:
                    # Departmental stats
                    dept_id = transcript_data.department # Using dept_id as key
                    if dept_id not in stats['departments']:
                        stats['departments'][dept_id] = {'count': 0, 'avg_cgpa': 0.0, 'total_cgpa_sum': 0.0, 'name': transcript_data.department_name}
                    
                    stats['departments'][dept_id]['count'] += 1
                    stats['departments'][dept_id]['total_cgpa_sum'] += transcript_data.overall_cgpa

                    # Overall CGPA stats
                    if transcript_data.overall_cgpa is not None: # Assuming CGPA can be None if no courses
                        total_cgpa_sum_for_avg += transcript_data.overall_cgpa
                        valid_cgpa_students_count += 1

                    # Grade distribution from latest grades contributing to CGPA
                    for grade_obj in transcript_data.latest_grades.values():
                        if self.grade_calculator.is_gpa_grade(grade_obj.grade): # Only count GPA-affecting grades
                            grade_letter = grade_obj.grade
                            stats['grade_distribution'][grade_letter] = stats['grade_distribution'].get(grade_letter, 0) + 1
            except Exception as e:
                print(f"Error processing student {student_id} for statistics: {e}")

        # Calculate averages
        if valid_cgpa_students_count > 0:
            stats['average_cgpa'] = total_cgpa_sum_for_avg / valid_cgpa_students_count

        for dept_id_key in stats['departments']: # Iterate over keys
            dept_info = stats['departments'][dept_id_key]
            if dept_info['count'] > 0:
                dept_info['avg_cgpa'] = dept_info['total_cgpa_sum'] / dept_info['count']
            del dept_info['total_cgpa_sum'] # Clean up temporary sum

        return stats


def main():
    """
    Main function for testing the transcript generator
    """
    print("=== Transcript Generator Test ===")

    # Initialize the transcript generator
    # Ensure database.py has been run to create and populate the DB
    db_file = "transcript_system.db"
    if not os.path.exists(db_file):
        print(f"Database file '{db_file}' not found. Please run database.py first to create and populate sample data.")
        # Consider if you want to offer to run it, or just exit. For now, just informing.
        # For example, you could try:
        # from database import TranscriptDatabase
        # print("Attempting to create and populate database...")
        # db_setup = TranscriptDatabase(db_file)
        # db_setup.populate_sample_data() # Make sure populate_sample_data is safe to call multiple times if needed
        # print("Database setup complete.")
        # Or simply:
        return 

    generator = TranscriptGenerator(db_path=db_file)

    all_students = generator.database.get_all_students()
    if not all_students:
        print("No students found in the database even after setup. Check database.py and its population logic.")
        return

    # Test single student transcript
    # Pick a student expected to have data, e.g., from SNG department if populated by database.py
    sample_student_id = None
    # Try to find a student, perhaps the first one from a known department
    # This depends on how database.py populates IDs
    if any("SNG" in s for s in all_students): # Example: pick an SNG student if any
        sample_student_id = next((s for s in all_students if "SNG" in s), all_students[0])
    else:
        sample_student_id = all_students[0]

    print(f"\nGenerating transcript for a sample student: {sample_student_id}")
    transcript_data = generator.generate_student_transcript(sample_student_id)
    if transcript_data:
        generator.print_transcript_summary(transcript_data)
    else:
        print(f"Could not generate transcript for sample student {sample_student_id}.")


    # Test department statistics
    print(f"\n{'=' * 60}")
    print("SYSTEM STATISTICS")
    print(f"{'=' * 60}")

    stats = generator.get_transcript_statistics()
    print(f"Total Students: {stats['total_students']}")
    print(f"Overall Average CGPA: {stats['average_cgpa']:.2f}")

    print(f"\nDepartment Breakdown:")
    if stats['departments']:
        for dept_id, info in stats['departments'].items():
            # Using .get for name in case it wasn't added, though it should be by the fixed get_transcript_statistics
            dept_name_display = info.get('name', dept_id) 
            print(f"  {dept_name_display} ({dept_id}): {info['count']} students, Avg CGPA: {info['avg_cgpa']:.2f}")
    else:
        print("  No department statistics available.")

    print(f"\nGrade Distribution (from latest attempts):")
    if stats['grade_distribution']:
        for grade, count in sorted(stats['grade_distribution'].items()):
            print(f"  {grade}: {count}")
    else:
        print("  No grade distribution data available.")

    # Test department transcript data generation
    print(f"\n{'=' * 60}")
    print("DEPARTMENT TRANSCRIPT DATA GENERATION TEST")
    print(f"{'=' * 60}")

    if stats['departments']:
        # Get first department ID from the statistics gathered
        first_dept_id = list(stats['departments'].keys())[0]
        first_dept_name = stats['departments'][first_dept_id].get('name', first_dept_id)
        print(f"Generating transcript data for department: {first_dept_name} ({first_dept_id})")

        # This method now returns List[TranscriptData]
        dept_transcript_data_list = generator.generate_department_transcripts(first_dept_id)
        print(f"Generated data for {len(dept_transcript_data_list)} transcripts for {first_dept_name}")
        # You could print a summary for the first student in this list if desired:
        # if dept_transcript_data_list:
        #     generator.print_transcript_summary(dept_transcript_data_list[0])
    else:
        print("No departments found to test department transcript generation.")


if __name__ == "__main__":
    main()