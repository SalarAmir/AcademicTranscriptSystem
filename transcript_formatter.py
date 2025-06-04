"""
Transcript Formatter for METU NCC Transcript System
Generates professional PDF and HTML transcripts
"""

import os
from typing import List, Optional, Dict, Any # Added Dict for consistency and Any for type annotations
from transcript_generator import TranscriptData # Corrected import, only TranscriptData is used
from datetime import datetime
# import webbrowser # webbrowser was not used

# ReportLab imports
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors


class TranscriptFormatter:
    """
    Handles formatting and generation of transcript documents
    Supports both HTML and PDF formats
    """

    def __init__(self, output_dir: str = "transcripts"):
        self.output_dir = output_dir
        self.ensure_output_directory()

    def ensure_output_directory(self):
        """Create output directory if it doesn't exist"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            print(f"Created output directory: {self.output_dir}")

    def generate_html_transcript(self, transcript_data: TranscriptData) -> str:
        """
        Generate HTML transcript and return file path
        """
        html_content = self._create_html_content(transcript_data)

        filename = f"{transcript_data.student_id}_transcript.html"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)

        return filepath

    def _create_html_content(self, transcript_data: TranscriptData) -> str:
        """
        Create the HTML content for a transcript
        """
        # Using the HTML structure you provided in the last file upload
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Official Transcript - {transcript_data.full_name}</title>
    <style>
        body {{
            font-family: 'Times New Roman', serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
            color: #333;
        }}

        .transcript-container {{
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 40px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            border: 1px solid #ddd;
        }}

        .header {{
            text-align: center;
            border-bottom: 3px solid #003366;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}

        .university-name {{
            font-size: 24px;
            font-weight: bold;
            color: #003366;
            margin-bottom: 5px;
        }}

        .document-title {{
            font-size: 20px;
            font-weight: bold;
            color: #666;
            margin-bottom: 10px;
        }}

        .student-info {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
            padding: 20px;
            background-color: #f9f9f9;
            border-left: 4px solid #003366;
        }}

        .info-item {{
            margin-bottom: 8px;
        }}

        .info-label {{
            font-weight: bold;
            color: #003366;
        }}

        .academic-summary {{
            margin-bottom: 30px;
            padding: 15px;
            background-color: #e8f4fd;
            border-radius: 5px;
        }}

        .summary-title {{
            font-size: 18px;
            font-weight: bold;
            color: #003366;
            margin-bottom: 10px;
        }}

        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
        }}

        .semester-section {{
            margin-bottom: 25px;
        }}

        .semester-title {{
            font-size: 16px;
            font-weight: bold;
            color: #003366;
            padding: 8px 12px;
            background-color: #f0f0f0;
            border-left: 4px solid #003366;
            margin-bottom: 10px;
        }}

        .courses-table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 15px;
        }}

        .courses-table th {{
            background-color: #003366;
            color: white;
            padding: 10px 8px;
            text-align: left;
            font-size: 14px;
        }}

        .courses-table td {{
            padding: 8px;
            border-bottom: 1px solid #ddd;
            font-size: 13px;
        }}

        .courses-table tr:hover {{
            background-color: #f5f5f5;
        }}

        .semester-summary {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            padding: 10px;
            background-color: #f9f9f9;
            border-radius: 3px;
            margin-bottom: 15px;
            font-size: 14px;
        }}

        .summary-item {{
            text-align: center;
        }}

        .summary-value {{
            font-weight: bold;
            color: #003366;
            font-size: 16px;
        }}

        .grade-excellent {{ color: #008000; font-weight: bold; }}
        .grade-good {{ color: #4CAF50; font-weight: bold; }}
        .grade-average {{ color: #FF9800; font-weight: bold; }}
        .grade-poor {{ color: #f44336; font-weight: bold; }}
        .grade-exempt {{ color: #9C27B0; font-weight: bold; }}

        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #003366;
            text-align: center;
            font-size: 12px;
            color: #666;
        }}

        .print-info {{
            margin-top: 30px;
            text-align: right;
            font-size: 12px;
            color: #999;
        }}

        @media print {{
            body {{ background-color: white; }}
            .transcript-container {{ box-shadow: none; border: none; }}
        }}
    </style>
</head>
<body>
    <div class="transcript-container">
        <div class="header">
            <div class="university-name">MIDDLE EAST TECHNICAL UNIVERSITY</div>
            <div class="university-name">NORTHERN CYPRUS CAMPUS</div>
            <div class="document-title">{transcript_data.transcript_type}</div>
        </div>

        <div class="student-info">
            <div>
                <div class="info-item">
                    <span class="info-label">Student ID:</span> {transcript_data.student_id}
                </div>
                <div class="info-item">
                    <span class="info-label">Full Name:</span> {transcript_data.full_name}
                </div>
                <div class="info-item">
                    <span class="info-label">Department:</span> {transcript_data.department_name}
                </div>
            </div>
            <div>
                <div class="info-item">
                    <span class="info-label">Curriculum:</span> {transcript_data.curriculum_version} ({transcript_data.curriculum_name or ''})
                </div>
                <div class="info-item">
                    <span class="info-label">Academic Standing:</span> {transcript_data.academic_standing}
                </div>
                <div class="info-item">
                    <span class="info-label">Generated:</span> {transcript_data.generation_date}
                </div>
            </div>
        </div>

        <div class="academic-summary">
            <div class="summary-title">Academic Summary</div>
            <div class="summary-grid">
                <div class="info-item">
                    <span class="info-label">Cumulative GPA:</span> <span class="summary-value">{transcript_data.overall_cgpa:.2f}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Credits Completed (GPA):</span> <span class="summary-value">{transcript_data.total_credits_completed:.1f}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Credits Passed (GPA):</span> <span class="summary-value">{transcript_data.total_credits_passed:.1f}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Completion Rate:</span> <span class="summary-value">{(transcript_data.total_credits_passed / 120.0 * 100.0) if 120.0 > 0 else 0.0:.1f}%</span>
                </div>
            </div>
        </div>

        <div class="academic-record">
            <h3 style="color: #003366; border-bottom: 2px solid #003366; padding-bottom: 5px;">Academic Record</h3>
            {self._generate_semester_sections(transcript_data)}
        </div>

        <div class="footer">
            <p><strong>MIDDLE EAST TECHNICAL UNIVERSITY - NORTHERN CYPRUS CAMPUS</strong></p>
            <p>This transcript is generated electronically and is valid without signature.</p>
            <p>For verification, contact the Registrar's Office at registrar@ncc.metu.edu.tr</p>
        </div>

        <div class="print-info">
            Document generated on {datetime.now().strftime("%Y-%m-%d at %H:%M:%S")}
        </div>
    </div>
</body>
</html>
"""
        return html

    def _generate_semester_sections(self, transcript_data: TranscriptData) -> str:
        """Generate HTML for all semester sections"""
        sections_html = ""
        if not transcript_data.semester_summaries:
            return "<p>No semester data found.</p>"

        for semester in sorted(transcript_data.semester_summaries.keys()):
            summary = transcript_data.semester_summaries[semester]
            sections_html += f"""
            <div class="semester-section">
                <div class="semester-title">{semester}</div>

                <div class="semester-summary">
                    <div class="summary-item">
                        <div>Semester GPA</div>
                        <div class="summary-value">{summary.get('semester_gpa', 0.0):.2f}</div>
                    </div>
                    <div class="summary-item">
                        <div>Cumulative GPA</div>
                        <div class="summary-value">{summary.get('cumulative_gpa', 0.0):.2f}</div>
                    </div>
                    <div class="summary-item">
                        <div>Semester Credits</div>
                        <div class="summary-value">{summary.get('semester_credits', 0.0):.1f}</div>
                    </div>
                    <div class="summary-item">
                        <div>Total Credits</div> <!-- This is cumulative_credits for that semester -->
                        <div class="summary-value">{summary.get('cumulative_credits', 0.0):.1f}</div>
                    </div>
                </div>

                <table class="courses-table">
                    <thead>
                        <tr>
                            <th>Course Code</th>
                            <th>Course Title</th>
                            <th>Credits</th>
                            <th>Grade</th>
                            <th>Points</th>
                        </tr>
                    </thead>
                    <tbody>
                        {self._generate_course_rows(summary.get('courses', []))}
                    </tbody>
                </table>
            </div>
            """
        return sections_html

    def _generate_course_rows(self, courses: List) -> str: # courses is List[CourseGrade]
        """Generate HTML table rows for courses"""
        rows_html = ""
        if not courses:
            return "<tr><td colspan='5'>No courses recorded for this semester.</td></tr>"

        for course in courses: # Each course is a CourseGrade object
            grade_class = self._get_grade_css_class(course.grade)
            # Ensure all attributes exist, falling back to "N/A" or 0.0 if necessary
            course_code = getattr(course, 'course_code', 'N/A')
            course_name = getattr(course, 'course_name', 'N/A')
            credit_hours = getattr(course, 'credit_hours', 0.0)
            grade = getattr(course, 'grade', 'N/A')
            grade_points = getattr(course, 'grade_points', 0.0)

            rows_html += f"""
                <tr>
                    <td>{course_code}</td>
                    <td>{course_name}</td>
                    <td>{credit_hours:.1f}</td>
                    <td><span class="{grade_class}">{grade}</span></td>
                    <td>{grade_points:.2f}</td>
                </tr>
            """
        return rows_html

    def _get_grade_css_class(self, grade: str) -> str:
        """Get CSS class for grade styling"""
        grade_upper = grade.upper() if grade else ""
        if grade_upper in ['AA', 'BA']:
            return 'grade-excellent'
        elif grade_upper in ['BB', 'CB']:
            return 'grade-good'
        elif grade_upper in ['CC', 'DC', 'DD']:
            return 'grade-average'
        elif grade_upper in ['FF', 'FD', 'NA']: # 'NA' might also be a failing grade
            return 'grade-poor'
        elif grade_upper in ['EX', 'P']:
            return 'grade-exempt'
        # For other grades like W, I, U, no specific class or a default one
        return ''

    def generate_pdf_transcript(self, transcript_data: TranscriptData) -> Optional[str]:
        """
        Generate PDF transcript (requires reportlab library)
        """
        try:
            filename = f"{transcript_data.student_id}_transcript.pdf"
            filepath = os.path.join(self.output_dir, filename)

            doc = SimpleDocTemplate(filepath, pagesize=A4,
                                    rightMargin=0.75*inch, leftMargin=0.75*inch,
                                    topMargin=0.75*inch, bottomMargin=0.75*inch)
            story: List[Any] = [] # Ensure story is typed for clarity
            styles = getSampleStyleSheet()

            # Define styles
            style_title = ParagraphStyle('Title', parent=styles['h1'], fontSize=14, alignment=1, spaceAfter=8, textColor=colors.HexColor('#003366'), leading=16)
            style_doc_title = ParagraphStyle('DocTitle', parent=style_title, fontSize=12, spaceAfter=16)
            style_heading = ParagraphStyle('Heading', parent=styles['h2'], fontSize=12, spaceAfter=6, textColor=colors.HexColor('#003366'), leading=14)
            style_semester_title = ParagraphStyle('SemesterTitle', parent=styles['h3'], fontSize=11, spaceBefore=10, spaceAfter=4, textColor=colors.HexColor('#003366'), leading=13)
            style_body = ParagraphStyle('Body', parent=styles['Normal'], fontSize=9, leading=11)
            style_table_header = ParagraphStyle('TableHeader', parent=style_body, fontName='Helvetica-Bold')
            style_footer = ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, alignment=1, textColor=colors.grey, leading=10)

            # 1. Transcript Header
            story.append(Paragraph("MIDDLE EAST TECHNICAL UNIVERSITY", style_title))
            story.append(Paragraph("NORTHERN CYPRUS CAMPUS", style_title))
            story.append(Paragraph(transcript_data.transcript_type.upper(), style_doc_title))
            story.append(Spacer(1, 0.20 * inch))

            # 2. Student Information Table
            student_info_data = [
                [Paragraph('<b>Student ID:</b>', style_body), Paragraph(transcript_data.student_id or 'N/A', style_body),
                 Paragraph('<b>Full Name:</b>', style_body), Paragraph(transcript_data.full_name or 'N/A', style_body)],
                [Paragraph('<b>Department:</b>', style_body), Paragraph(transcript_data.department_name or 'N/A', style_body),
                 Paragraph('<b>Curriculum:</b>', style_body), Paragraph(f"{transcript_data.curriculum_version or 'N/A'} ({transcript_data.curriculum_name or ''})", style_body)],
                [Paragraph('<b>Overall CGPA:</b>', style_body), Paragraph(f"{transcript_data.overall_cgpa:.2f}" if transcript_data.overall_cgpa is not None else "N/A", style_body),
                 Paragraph('<b>Academic Standing:</b>', style_body), Paragraph(transcript_data.academic_standing or 'N/A', style_body)],
                [Paragraph('<b>Total Credits Passed (GPA):</b>', style_body), Paragraph(f"{transcript_data.total_credits_passed:.1f}" if transcript_data.total_credits_passed is not None else "N/A", style_body),
                 Paragraph('<b>Date Generated:</b>', style_body), Paragraph(transcript_data.generation_date or 'N/A', style_body)],
            ]
            student_info_table = Table(student_info_data, colWidths=[1.4*inch, 2.1*inch, 1.4*inch, 2.1*inch])
            student_info_table.setStyle(TableStyle([
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('LEFTPADDING', (0,0), (-1,-1), 4),
                ('RIGHTPADDING', (0,0), (-1,-1), 4),
                ('TOPPADDING', (0,0), (-1,-1), 3),
                ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ]))
            story.append(student_info_table)
            story.append(Spacer(1, 0.20 * inch))

            # 3. Academic Record Section
            story.append(Paragraph("Academic Record", style_heading))

            sorted_semesters = sorted(transcript_data.semester_summaries.keys()) if transcript_data.semester_summaries else []
            
            if not sorted_semesters:
                story.append(Paragraph("No academic records found for this student.", style_body))

            for semester in sorted_semesters:
                summary = transcript_data.semester_summaries.get(semester, {}) # Default to empty dict
                
                story.append(Paragraph(semester, style_semester_title))
                
                sem_gpa = summary.get('semester_gpa', 0.0)
                sem_credits = summary.get('semester_credits', 0.0)
                sem_points = summary.get('semester_points', 0.0) # Assuming this is in summary
                cum_gpa = summary.get('cumulative_gpa', 0.0)

                sem_summary_line = f"GPA: {sem_gpa:.2f} | Credits: {sem_credits:.1f} | Points: {sem_points:.1f} | CGPA (End of Sem): {cum_gpa:.2f}"
                story.append(Paragraph(sem_summary_line, style_body))
                story.append(Spacer(1, 0.05 * inch))

                course_header = [
                    Paragraph('Code', style_table_header), Paragraph('Course Title', style_table_header),
                    Paragraph('CR', style_table_header), Paragraph('Grade', style_table_header),
                    Paragraph('Points', style_table_header) # Course quality points
                ]
                course_data_rows = [course_header]

                semester_courses = summary.get('courses', []) # List[CourseGrade]
                if not semester_courses:
                    course_data_rows.append([Paragraph("No courses recorded for this semester.", style_body), "", "", "", ""])
                else:
                    for course in semester_courses: # course is expected to be CourseGrade object
                        course_data_rows.append([
                            Paragraph(getattr(course, 'course_code', 'N/A'), style_body),
                            Paragraph(getattr(course, 'course_name', 'N/A'), style_body),
                            Paragraph(f"{getattr(course, 'credit_hours', 0.0):.1f}", style_body),
                            Paragraph(getattr(course, 'grade', 'N/A'), style_body),
                            Paragraph(f"{getattr(course, 'grade_points', 0.0):.2f}", style_body)
                        ])
                
                courses_table = Table(course_data_rows, colWidths=[0.7*inch, 3.0*inch, 0.5*inch, 0.6*inch, 0.7*inch])
                courses_table.setStyle(TableStyle([
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey), # Header row background
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('LEFTPADDING', (0,0), (-1,-1), 3),
                    ('RIGHTPADDING', (0,0), (-1,-1), 3),
                    ('TOPPADDING', (0,0), (-1,-1), 2),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
                ]))
                story.append(courses_table)
                story.append(Spacer(1, 0.15 * inch))

            # 4. Transcript Footer
            story.append(Spacer(1, 0.3 * inch))
            footer_line = Paragraph(f"End of Transcript. Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}. METU NCC.", style_footer)
            story.append(footer_line)

            doc.build(story)
            return filepath

        except ImportError:
            print("Error: Reportlab library not found. Cannot generate PDF.")
            print("Please install it: pip install reportlab")
            return None
        except Exception as e:
            import traceback # Ensure traceback is imported here if not globally
            student_id_for_error = transcript_data.student_id if transcript_data and hasattr(transcript_data, 'student_id') else 'Unknown'
            print(f"An error occurred during PDF generation for student {student_id_for_error}: {e}")
            traceback.print_exc()
            return None