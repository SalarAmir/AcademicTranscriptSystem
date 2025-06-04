"""
Grade Calculator for METU NCC Transcript System
Implements METU NCC Undergraduate Education Regulations - Article 24
"""

import functools
from typing import Dict, List, Tuple, Optional, Any # Add Any if not already there
from dataclasses import dataclass


@dataclass
class CourseGrade:
    """Represents a single course grade with all relevant information"""
    course_code: str
    course_name: str
    semester: str
    grade: str
    metu_credits: str  # Format: "4(3-2)"
    ects_credits: float
    attempt_number: int
    credit_hours: float = 0.0  # Extracted from metu_credits
    grade_points: float = 0.0  # Calculated based on grade


class GradeCalculator:
    """
    Handles all grade calculations according to METU NCC regulations
    """

    # METU Grade Scale (Article 24)
    GRADE_SCALE = {
        'AA': 4.0,
        'BA': 3.5,
        'BB': 3.0,
        'CB': 2.5,
        'CC': 2.0,
        'DC': 1.5,
        'DD': 1.0,
        'FF': 0.0,
        'FD': 0.0,  # Fail due to attendance
        'NA': 0.0,  # Not Attended
        'EX': None,  # Exempt - not included in GPA calculations
        'P': None,  # Pass - not included in GPA calculations
        'NP': None,  # Not Pass - not included in GPA calculations
        'W': None,  # Withdrawn - not included in GPA calculations
        'I': None,  # Incomplete - not included in GPA calculations
    }

    # Passing grades
    PASSING_GRADES = {'AA', 'BA', 'BB', 'CB', 'CC', 'DC', 'DD', 'P', 'EX'}

    # Grades that don't contribute to GPA calculation
    NON_GPA_GRADES = {'EX', 'P', 'NP', 'W', 'I'}

    def __init__(self):
        pass

    def extract_credit_hours(self, metu_credits: Optional[str]) -> float:
        """
        Extract credit hours from METU credit format
        Format examples: "4(3-2)", "3(3-0)", "0(2-0)"
        Returns the first number (total credit hours)
        Handles None or empty string for metu_credits by defaulting to '0'.
        """
        if not metu_credits:  # This will catch None or an empty string
            metu_credits = '0'
        
        try:
            # Ensure metu_credits is treated as a string from here
            metu_credits_str = str(metu_credits) 
            if '(' in metu_credits_str:
                return float(metu_credits_str.split('(')[0])
            else:
                return float(metu_credits_str)
        except (ValueError, IndexError):
            # If conversion still fails, default to 0.0 and perhaps log a warning
            # print(f"Warning: Could not parse metu_credits '{metu_credits}'. Defaulting to 0.0 credit hours.")
            return 0.0

    def get_grade_points(self, grade: str) -> Optional[float]:
        """
        Get grade points for a given grade
        Returns None for grades that don't contribute to GPA
        """
        return self.GRADE_SCALE.get(grade.upper())

    def is_passing_grade(self, grade: str) -> bool:
        """Check if a grade is passing"""
        return grade.upper() in self.PASSING_GRADES

    def is_gpa_grade(self, grade: str) -> bool:
        """Check if a grade contributes to GPA calculation"""
        return grade.upper() not in self.NON_GPA_GRADES

    def process_course_grades(self, enrollments: List[Dict]) -> List[CourseGrade]:
        """
        Process raw enrollment data into CourseGrade objects
        """
        course_grades = []

        for enrollment in enrollments:
            # Extract credit hours from METU credits format
            credit_hours = self.extract_credit_hours(enrollment.get('metu_credits', '0'))

            # Calculate grade points
            grade_points = self.get_grade_points(enrollment['grade'])
            if grade_points is not None:
                grade_points = grade_points * credit_hours
            else:
                grade_points = 0.0

            course_grade = CourseGrade(
                course_code=enrollment['course_code'],
                course_name=enrollment['course_name'],
                semester=enrollment['semester'],
                grade=enrollment['grade'],
                metu_credits=enrollment.get('metu_credits', ''),
                ects_credits=enrollment.get('ects_credits', 0.0),
                attempt_number=enrollment.get('attempt_number', 1),
                credit_hours=credit_hours,
                grade_points=grade_points
            )

            course_grades.append(course_grade)

        return course_grades

    def get_latest_grades(self, course_grades: List[CourseGrade]) -> Dict[str, CourseGrade]:
        """
        Get the latest grade for each course (handles repeated courses)
        Returns a dictionary with course_code as key and latest CourseGrade as value
        """
        latest_grades = {}

        for grade in course_grades:
            course_code = grade.course_code

            if course_code not in latest_grades:
                latest_grades[course_code] = grade
            else:
                # Compare by semester and attempt number to find the latest
                current = latest_grades[course_code]

                # Simple semester comparison (assumes format like "2024-Fall", "2024-Spring")
                if self._compare_semesters(grade.semester, current.semester) > 0:
                    latest_grades[course_code] = grade
                elif (self._compare_semesters(grade.semester, current.semester) == 0 and
                      grade.attempt_number > current.attempt_number):
                    latest_grades[course_code] = grade

        return latest_grades

    def _compare_semesters(self, sem1: str, sem2: str) -> int:
        """
        Compare two semesters
        Returns: 1 if sem1 > sem2, -1 if sem1 < sem2, 0 if equal
        Format: "2024-Fall", "2024-Spring"
        """
        try:
            year1, season1 = sem1.split('-')
            year2, season2 = sem2.split('-')

            year1, year2 = int(year1), int(year2)

            if year1 != year2:
                return 1 if year1 > year2 else -1

            # Same year, compare seasons
            season_order = {'Spring': 1, 'Summer': 2, 'Fall': 3}
            season1_val = season_order.get(season1, 0)
            season2_val = season_order.get(season2, 0)

            if season1_val > season2_val:
                return 1
            elif season1_val < season2_val:
                return -1
            else:
                return 0

        except (ValueError, IndexError):
            return 0

    def calculate_semester_gpa(self, course_grades: List[CourseGrade]) -> Tuple[float, float, float]:
        """
        Calculate GPA for a specific semester
        Returns: (GPA, total_points, total_credits)
        """
        total_points = 0.0
        total_credits = 0.0

        for grade in course_grades:
            if self.is_gpa_grade(grade.grade):
                grade_point_value = self.get_grade_points(grade.grade)
                if grade_point_value is not None:
                    total_points += grade_point_value * grade.credit_hours
                    total_credits += grade.credit_hours

        gpa = total_points / total_credits if total_credits > 0 else 0.0
        return round(gpa, 2), total_points, total_credits

    def calculate_cgpa(self, course_grades: List[CourseGrade]) -> Tuple[float, float, float]:
        """
        Calculate Cumulative GPA (CGPA) considering only the latest grade for each course
        Returns: (CGPA, total_points, total_credits)
        """
        # Get latest grades for each course
        latest_grades = self.get_latest_grades(course_grades)

        total_points = 0.0
        total_credits = 0.0

        for grade in latest_grades.values():
            if self.is_gpa_grade(grade.grade):
                grade_point_value = self.get_grade_points(grade.grade)
                if grade_point_value is not None:
                    total_points += grade_point_value * grade.credit_hours
                    total_credits += grade.credit_hours

        cgpa = total_points / total_credits if total_credits > 0 else 0.0
        return round(cgpa, 2), total_points, total_credits

    def group_grades_by_semester(self, course_grades: List[CourseGrade]) -> Dict[str, List[CourseGrade]]:
        """
        Group course grades by semester
        Returns dictionary with semester as key and list of CourseGrade as value
        """
        semester_grades = {}

        for grade in course_grades:
            semester = grade.semester
            if semester not in semester_grades:
                semester_grades[semester] = []
            semester_grades[semester].append(grade)

        return semester_grades

    def calculate_semester_summary(self, semester_grades: Dict[str, List[CourseGrade]]) -> Dict[str, Dict[str, Any]]:
        """
        Calculate summary statistics for each semester, ensuring chronological processing
        for accurate running cumulative totals.
        """
        summary_output: Dict[str, Dict[str, Any]] = {}
        
        # Sort semester keys chronologically using your existing _compare_semesters method
        # This is crucial for calculating running totals correctly.
        if not semester_grades:
            return summary_output
            
        sorted_semester_keys = sorted(semester_grades.keys(), key=functools.cmp_to_key(self._compare_semesters))

        # This list will accumulate all CourseGrade objects chronologically
        # to correctly calculate CGPA at the end of each semester.
        all_grades_processed_chronologically: List[CourseGrade] = []

        for semester_key in sorted_semester_keys:
            grades_this_semester = semester_grades.get(semester_key, []) # Get grades for the current semester
            
            # Calculate stats for the current semester
            current_semester_gpa, current_semester_quality_points, current_semester_gpa_credits = \
                self.calculate_semester_gpa(grades_this_semester)

            # Add this semester's grades to our running list of all grades processed so far
            all_grades_processed_chronologically.extend(grades_this_semester)
            
            # Calculate CGPA and cumulative points/credits based on *all* grades processed up to this point.
            # self.calculate_cgpa returns: (CGPA, total_quality_points_for_cgpa, total_gpa_credits_for_cgpa)
            # These are cumulative values considering only the latest attempts of courses.
            cgpa_at_end_of_semester, cumulative_q_points, cumulative_gpa_credits_val = \
                self.calculate_cgpa(all_grades_processed_chronologically)

            summary_output[semester_key] = {
                'semester_gpa': current_semester_gpa,
                'semester_points': current_semester_quality_points,        # Quality points for this semester
                'semester_credits': current_semester_gpa_credits,      # GPA Credits for this semester
                'cumulative_gpa_at_semester_end': cgpa_at_end_of_semester,
                'cumulative_quality_points_at_semester_end': cumulative_q_points, # CORRECTED: Use variable from calculate_cgpa
                'cumulative_gpa_credits_at_semester_end': cumulative_gpa_credits_val,    # CORRECTED: Use variable from calculate_cgpa
                'courses': grades_this_semester # List of CourseGrade objects for this semester
            }
        return summary_output

    def get_academic_standing(self, cgpa: float) -> str:
        """
        Determine academic standing based on CGPA
        """
        if cgpa >= 3.5:
            return "Dean's List"
        elif cgpa >= 3.0:
            return "Honor Roll"
        elif cgpa >= 2.0:
            return "Good Standing"
        elif cgpa >= 1.5:
            return "Academic Warning"
        else:
            return "Academic Probation"

    def calculate_completion_status(self, course_grades: List[CourseGrade],
                                    required_credits: float = 120.0) -> Dict[str, float]:
        """
        Calculate degree completion status
        """
        latest_grades = self.get_latest_grades(course_grades)

        completed_credits = 0.0
        passed_credits = 0.0

        for grade in latest_grades.values():
            if self.is_gpa_grade(grade.grade):
                completed_credits += grade.credit_hours
                if self.is_passing_grade(grade.grade):
                    passed_credits += grade.credit_hours

        completion_percentage = (passed_credits / required_credits) * 100.0

        return {
            'completed_credits': completed_credits,
            'passed_credits': passed_credits,
            'required_credits': required_credits,
            'completion_percentage': min(completion_percentage, 100.0)
        }


if __name__ == "__main__":
    # Test the grade calculator
    calculator = GradeCalculator()

    # Sample test data
    sample_enrollments = [
        {
            'course_code': '3890111',
            'course_name': 'INTRO TO COMPUTER SCIENCE',
            'semester': '2023-Fall',
            'grade': 'AA',
            'metu_credits': '4(3-2)',
            'ects_credits': 6.0,
            'attempt_number': 1
        },
        {
            'course_code': '3570119',
            'course_name': 'CALCULUS',
            'semester': '2023-Fall',
            'grade': 'BB',
            'metu_credits': '5(4-2)',
            'ects_credits': 7.5,
            'attempt_number': 1
        },
        {
            'course_code': '3570119',  # Repeated course
            'course_name': 'CALCULUS',
            'semester': '2024-Spring',
            'grade': 'AA',
            'metu_credits': '5(4-2)',
            'ects_credits': 7.5,
            'attempt_number': 2
        }
    ]

    # Process grades
    course_grades = calculator.process_course_grades(sample_enrollments)

    print("=== Grade Calculator Test ===")
    print(f"Processed {len(course_grades)} course grades")

    # Test semester GPA
    semester_grades = calculator.group_grades_by_semester(course_grades)
    for semester, grades in semester_grades.items():
        gpa, points, credits = calculator.calculate_semester_gpa(grades)
        print(f"{semester}: GPA = {gpa}, Credits = {credits}")

    # Test CGPA
    cgpa, total_points, total_credits = calculator.calculate_cgpa(course_grades)
    print(f"CGPA: {cgpa} ({total_points} points, {total_credits} credits)")

    # Test latest grades
    latest = calculator.get_latest_grades(course_grades)
    print(f"Latest grades for {len(latest)} unique courses")
    for code, grade in latest.items():
        print(f"  {code}: {grade.grade} (Semester: {grade.semester})")