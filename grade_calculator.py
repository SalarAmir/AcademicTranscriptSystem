import functools
from typing import Dict, List, Tuple, Optional, Any
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
    GRADE_SCALE = {
        'AA': 4.0, 'BA': 3.5, 'BB': 3.0, 'CB': 2.5, 'CC': 2.0,
        'DC': 1.5, 'DD': 1.0, 'FD': 0.0, 'FF': 0.0, 'NA': 0.0,
        'EX': None, 'P': None, 'NP': None, 'W': None, 'I': None,
    }
    PASSING_GRADES = {'AA', 'BA', 'BB', 'CB', 'CC', 'DC', 'DD', 'P', 'EX'}
    NON_GPA_GRADES = {'EX', 'P', 'NP', 'W', 'I'}

    def extract_credit_hours(self, metu_credits: Optional[str]) -> float:
        """Extracts credit hours from METU credit format like "4(3-2)"."""
        if not metu_credits:
            return 0.0
        try:
            metu_credits_str = str(metu_credits)
            if '(' in metu_credits_str:
                return float(metu_credits_str.split('(')[0])
            else:
                return float(metu_credits_str)
        except (ValueError, IndexError):
            return 0.0

    def get_grade_points(self, grade: str) -> Optional[float]:
        """Get grade points for a given grade"""
        return self.GRADE_SCALE.get(grade.upper())

    def is_passing_grade(self, grade: str) -> bool:
        """Check if a grade is a passing grade"""
        return grade.upper() in self.PASSING_GRADES

    def is_gpa_grade(self, grade: str) -> bool:
        """Check if a grade contributes to GPA calculation"""
        return grade.upper() not in self.NON_GPA_GRADES

    def process_course_grades(self, enrollments: List[Dict]) -> List[CourseGrade]:
        """Process raw enrollment data into a list of CourseGrade objects"""
        course_grades = []
        for enrollment in enrollments:
            credit_hours = self.extract_credit_hours(enrollment.get('metu_credits'))
            grade_points_value = self.get_grade_points(enrollment['grade'])
            
            course_grade = CourseGrade(
                course_code=enrollment['course_code'],
                course_name=enrollment['course_name'],
                semester=enrollment['semester'],
                grade=enrollment['grade'],
                metu_credits=enrollment.get('metu_credits', ''),
                ects_credits=enrollment.get('ects_credits', 0.0),
                attempt_number=enrollment.get('attempt_number', 1),
                credit_hours=credit_hours,
                grade_points=(grade_points_value * credit_hours) if grade_points_value is not None else 0.0
            )
            course_grades.append(course_grade)
        return course_grades

    def _compare_semesters(self, sem1: str, sem2: str) -> int:
        """Compare two semesters (e.g., "2023-Fall" > "2023-Spring")."""
        try:
            year1, season1 = sem1.split('-')
            year2, season2 = sem2.split('-')
            year1, year2 = int(year1), int(year2)

            if year1 != year2:
                return 1 if year1 > year2 else -1
            
            season_order = {'Spring': 1, 'Summer': 2, 'Fall': 3}
            season1_val = season_order.get(season1, 0)
            season2_val = season_order.get(season2, 0)

            if season1_val > season2_val: return 1
            elif season1_val < season2_val: return -1
            else: return 0
        except (ValueError, IndexError):
            return 0 # Treat as equal if format is unexpected

    def get_latest_grades(self, course_grades: List[CourseGrade]) -> Dict[str, CourseGrade]:
        """Get the latest grade for each course (handles repeated courses)"""
        latest_grades: Dict[str, CourseGrade] = {}
        sorted_grades = sorted(course_grades, key=lambda g: (g.semester, g.attempt_number), reverse=True)

        for grade in sorted_grades:
            if grade.course_code not in latest_grades:
                latest_grades[grade.course_code] = grade
        return latest_grades

    def calculate_semester_gpa(self, course_grades: List[CourseGrade]) -> Tuple[float, float, float]:
        """Calculate GPA for a specific semester"""
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
        """Calculate Cumulative GPA considering only the latest grade for each course"""
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
        """Group course grades by semester"""
        semester_grades: Dict[str, List[CourseGrade]] = {}
        for grade in course_grades:
            semester = grade.semester
            if semester not in semester_grades:
                semester_grades[semester] = []
            semester_grades[semester].append(grade)
        return semester_grades

    def calculate_semester_summary(self, semester_grades: Dict[str, List[CourseGrade]]) -> Dict[str, Dict[str, Any]]:
        """Calculate summary statistics for each semester with correct running CGPA."""
        summary_output: Dict[str, Dict[str, Any]] = {}
        if not semester_grades:
            return summary_output
            
        sorted_semester_keys = sorted(semester_grades.keys(), key=functools.cmp_to_key(self._compare_semesters))
        all_grades_processed_chronologically: List[CourseGrade] = []

        for semester_key in sorted_semester_keys:
            grades_this_semester = semester_grades.get(semester_key, [])
            
            sem_gpa, sem_points, sem_credits = self.calculate_semester_gpa(grades_this_semester)
            all_grades_processed_chronologically.extend(grades_this_semester)
            
            cgpa, cum_points, cum_credits = self.calculate_cgpa(all_grades_processed_chronologically)

            # FIX: Use consistent, simple keys for the dictionary
            summary_output[semester_key] = {
                'semester_gpa': sem_gpa,
                'semester_points': sem_points,
                'semester_credits': sem_credits,
                'cumulative_gpa': cgpa,         # Standardized key
                'cumulative_points': cum_points, # Standardized key
                'cumulative_credits': cum_credits, # Standardized key
                'courses': grades_this_semester
            }
        return summary_output
    
    def get_academic_standing(self, cgpa: float) -> str:
        """Determine academic standing based on CGPA."""
        if cgpa >= 3.5: return "High Honor"
        elif cgpa >= 3.0: return "Honor"
        elif cgpa >= 2.0: return "Satisfactory"
        elif cgpa >= 1.8: return "Probation"
        else: return "Unsatisfactory"

    def calculate_completion_status(self, course_grades: List[CourseGrade]) -> Dict[str, float]:
        """Calculate degree completion status based on passed credits."""
        latest_grades = self.get_latest_grades(course_grades)
        completed_credits = 0.0 # Credits for courses attempted and included in GPA
        passed_credits = 0.0    # Credits for courses passed

        for grade in latest_grades.values():
            if self.is_gpa_grade(grade.grade):
                completed_credits += grade.credit_hours
                if self.is_passing_grade(grade.grade):
                    passed_credits += grade.credit_hours
        
        return {
            'completed_credits': completed_credits,
            'passed_credits': passed_credits
        }
