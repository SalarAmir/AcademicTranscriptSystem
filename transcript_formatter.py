"""
Transcript Formatter for METU NCC Transcript System
Generates professional PDF and HTML transcripts
"""

import os
from typing import List, Optional
from transcript_generator import TranscriptGenerator, TranscriptData
from datetime import datetime
import webbrowser



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
                    <span class="info-label">Curriculum:</span> {transcript_data.curriculum_version}
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
                    <span class="info-label">Credits Completed:</span> <span class="summary-value">{transcript_data.total_credits_completed:.1f}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Credits Passed:</span> <span class="summary-value">{transcript_data.total_credits_passed:.1f}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Completion Rate:</span> <span class="summary-value">{(transcript_data.total_credits_passed / 120 * 100):.1f}%</span>
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

        for semester in sorted(transcript_data.semester_summaries.keys()):
            summary = transcript_data.semester_summaries[semester]
            sections_html += f"""
            <div class="semester-section">
                <div class="semester-title">{semester}</div>

                <div class="semester-summary">
                    <div class="summary-item">
                        <div>Semester GPA</div>
                        <div class="summary-value">{summary['semester_gpa']:.2f}</div>
                    </div>
                    <div class="summary-item">
                        <div>Cumulative GPA</div>
                        <div class="summary-value">{summary['cumulative_gpa']:.2f}</div>
                    </div>
                    <div class="summary-item">
                        <div>Semester Credits</div>
                        <div class="summary-value">{summary['semester_credits']:.1f}</div>
                    </div>
                    <div class="summary-item">
                        <div>Total Credits</div>
                        <div class="summary-value">{summary['cumulative_credits']:.1f}</div>
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
                        {self._generate_course_rows(summary['courses'])}
                    </tbody>
                </table>
            </div>
            """

        return sections_html

    def _generate_course_rows(self, courses: List) -> str:
        """Generate HTML table rows for courses"""
        rows_html = ""

        for course in courses:
            grade_class = self._get_grade_css_class(course.grade)
            rows_html += f"""
                <tr>
                    <td>{course.course_code}</td>
                    <td>{course.course_name}</td>
                    <td>{course.credit_hours:.1f}</td>
                    <td><span class="{grade_class}">{course.grade}</span></td>
                    <td>{course.grade_points:.2f}</td>
                </tr>
            """

        return rows_html

    def _get_grade_css_class(self, grade: str) -> str:
        """Get CSS class for grade styling"""
        if grade in ['AA', 'BA']:
            return 'grade-excellent'
        elif grade in ['BB', 'CB']:
            return 'grade-good'
        elif grade in ['CC', 'DC', 'DD']:
            return 'grade-average'
        elif grade in ['FF', 'FD']:
            return 'grade-poor'
        elif grade in ['EX', 'P']:
            return 'grade-exempt'
        else:
            return ''

    def generate_pdf_transcript(self, transcript_data: TranscriptData) -> Optional[str]:
        """
        Generate PDF transcript (requires reportlab library)
        """
        try:
            from reportlab.lib.pagesizes import letter, A4
            from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import inch
            from reportlab.lib import colors

            filename = f"{transcript_data.student_id}_transcript.pdf"
            filepath = os.path.join(self.output_dir, filename)

            # Create PDF document
            doc = SimpleDocTemplate(filepath, pagesize=A4,
                                    rightMargin=72, leftMargin=72,
                                    topMargin=72, bottomMargin=18)

            # Build story (content)
            story = []
            styles = getSampleStyleSheet()

            # Custom styles
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=16,
                spaceAfter=30,
                alignment=1,  # Center
                textColor=colors.HexColor('#003366')
            )

            heading_style = ParagraphStyle(
                'CustomHeading',
                parent=styles['Heading2'],
                fontSize=14,
                spaceAfter=12,
                textColor=colors.HexColor('#003366')
            )

            # Header
            story.append(Paragraph("MIDDLE EAST TECHNICAL UNIVERSITY", title_style))
            story.append(Paragraph("NORTHERN CYPRUS CAMPUS", title_style))
            story.append(Paragraph("OFFICIAL ACADEMIC TRANSCRIPT", title_style))
            story.append(Spacer(1, 20))

            # Student Information
            student_info = [
                ['Student ID:', transcript_data.student_id, 'Full Name:', transcript_data.full_name],
                ['Department:', transcript_data.department_name, 'Curriculum:', transcript_data.curriculum_version],
                ['CGPA:', f"{transcript_data.overall_cgpa:.2f}", 'Academic Standing:',
                 transcript_data.academic_standing],
                ['Credits Completed:', f"{transcript_data.total_credits_completed:.1f}", 'Credits Passed:',
                 f"{transcript_data.total_credits_passed:.1f}"]
            ]

            info_table = Table(student_info, colWidths=[1.2 * inch, 1.8 * inch, 1.2 * inch, 1.8 * inch])
            info_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f9f9f9')),
                ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#003366')),
                ('TEXTCOLOR', (2, 0), (2, -1), colors.HexColor('#003366')),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]))

            story.append(info_table)
            story.append(Spacer(1, 20))

            # Academic Record
            story.append(Paragraph("Academic Record", heading_style))

            # Semester by semester
            for semester in sorted(transcript_data.semester_summaries.keys()):
                summary = transcript_data.semester_summaries[semester]

                # Semester header
                story.append(Paragraph(f"<b>{semester}</b>", styles['Heading3']))

                # Course table
                course_data = [['Course Code', 'Course Title', 'Credits', 'Grade', 'Points']]

                for course in summary['courses']:
                    course_data.append

                # ... (previous code in generate_pdf_transcript) ...

            # Semester by semester
            for semester in sorted(transcript_data.semester_summaries.keys()):
                summary = transcript_data.semester_summaries[semester]

                # Semester header
                story.append(Paragraph(f"<b>{semester}</b>", styles['Heading3']))
                story.append(Spacer(1, 6)) # Add a small spacer

                # Course table header
                course_data = [['Course Code', 'Course Title', 'Credits', 'Grade', 'Points']]
                
                # Populate course data for the current semester
                for course in summary['courses']:
                    course_data.append([
                        course.course_code,
                        Paragraph(course.course_name, styles['Normal']), # Wrap long names
                        f"{course.credit_hours:.1f}",
                        course.grade,
                        f"{course.grade_points:.2f}"
                    ])
                
                # Create and style the course table
                semester_table = Table(course_data, colWidths=[0.8*inch, 2.5*inch, 0.6*inch, 0.5*inch, 0.6*inch])
                semester_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#003366')),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f9f9f9')),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ('FONTSIZE', (0,0), (-1,-1), 8), # Smaller font for table content
                ]))
                story.append(semester_table)
                story.append(Spacer(1, 12)) # Spacer after each semester table

            # Footer for PDF (optional, can be added similarly or using page templates)
            story.append(Spacer(1, 24))
            story.append(Paragraph(f"Transcript generated on: {transcript_data.generation_date}", styles['Normal']))
            story.append(Paragraph("MIDDLE EAST TECHNICAL UNIVERSITY - NORTHERN CYPRUS CAMPUS", styles['Normal']))


            doc.build(story)
            return filepath

        except ImportError:
            print("Error: Reportlab library not found. Cannot generate PDF.")
            print("Please install it: pip install reportlab")
            return None
        except Exception as e:
            print(f"An error occurred during PDF generation for {transcript_data.student_id}: {e}")
            return None
        
        