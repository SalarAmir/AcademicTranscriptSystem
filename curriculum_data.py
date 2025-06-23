# curriculum_data.py
import random
import os
"""
This file contains the embedded curriculum data for the SNG department.
It is imported by database.py to populate the curriculum tables.
"""
# curriculum_data.py

"""
This file contains the embedded curriculum data for the SNG department.
It is imported by database.py to populate the curriculum tables.
"""

SNG_CURRICULA_DATA = {
    1: [
        {'code': '3570119', 'name': 'Calculus with Analytic Geometry', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 1, 'prerequisites': ['3570100']},
        {'code': '3580105', 'name': 'General Physics I', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 1, 'prerequisites': []},
        {'code': '3550101', 'name': 'Comp. Engineering Orientation', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1, 'prerequisites': []},
        {'code': '3890111', 'name': 'Introduction to Comp. Engineering Concepts', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 1, 'prerequisites': []},
        {'code': '3600107', 'name': 'General Chemistry', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3590101', 'name': 'Development of Reading and Writing Skills I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3550100', 'name': 'Introduction to Computer Science and Programming', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1, 'prerequisites': []},
        {'code': '3530100', 'name': 'Career Planning', 'metu': '0(1-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570120', 'name': 'Calculus for Functions of Several Variables', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 2, 'prerequisites': ['3570119']},
        {'code': '3580106', 'name': 'General Physics II', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 2, 'prerequisites': []},
        {'code': '3890140', 'name': 'Programming', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570260', 'name': 'Basic Linear Algebra', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 2, 'prerequisites': []},
        {'code': '3590102', 'name': 'Development of Reading and Writing Skills II', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 2, 'prerequisites': ['3590101']},
        {'code': '3870101', 'name': 'Occupational Health and Safety-I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570219', 'name': 'Introduction to Differential Equations', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 3, 'prerequisites': ['3570120']},
        {'code': '3890201', 'name': 'Introduction To Software Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 3, 'prerequisites': []},
        {'code': '3550213', 'name': 'Data Structures', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 3, 'prerequisites': ['3890140']},
        {'code': '3550223', 'name': 'Discrete Computational Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 3, 'prerequisites': []},
        {'code': '3590211', 'name': 'Academic Oral Presentation Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 3, 'prerequisites': ['3590102']},
        {'code': '3610101', 'name': 'Turkish I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},
        {'code': '3620201', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},
        {'code': '3630221', 'name': 'Statistics for Engineers I', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4, 'prerequisites': ['3570120']},
        {'code': '3890242', 'name': 'Object Oriented Software Development', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4, 'prerequisites': ['3550213', '3890111']},
        {'code': '3550280', 'name': 'Formal Languages and Abstract Machines', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 4, 'prerequisites': ['3550223']},
        {'code': '3550232', 'name': 'Logic Design', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4, 'prerequisites': []},
        {'code': '3610102', 'name': 'Turkish II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4, 'prerequisites': ['3610101']},
        {'code': '3620202', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4, 'prerequisites': ['3620201']},
        {'code': '3890221', 'name': 'Software Requirements Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4, 'prerequisites': ['3890201']},
        {'code': '3550315', 'name': 'Algorithms', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5, 'prerequisites': ['3550213']},
        {'code': '3550331', 'name': 'Computer Organization', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5, 'prerequisites': ['3550232']},
        {'code': '3550351', 'name': 'Data Management and File Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5, 'prerequisites': []},
        {'code': '3590311', 'name': 'Advanced Communication Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 5, 'prerequisites': ['3590211']},
        {'code': '3890303', 'name': 'Software Project Management', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5, 'prerequisites': []},
        {'code': '3890330', 'name': 'Software Desing', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5, 'prerequisites': ['3890201', '3890242']},
        {'code': '3890300', 'name': 'Summer Practice I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5, 'prerequisites': ['3550100', '3870101']},
        {'code': '3870301', 'name': 'Occupational Health And Safesty II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5, 'prerequisites': []},
        {'code': '3550334', 'name': 'Introduction to Operating Systems', 'metu': '3(3-0)', 'ects': 5.5, 'sem': 6, 'prerequisites': ['3550331']},
        {'code': '3890341', 'name': 'Software Construction and Evolution', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 6, 'prerequisites': ['3890330']},
        {'code': '3890346', 'name': 'Web Aplication Development', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': ['3890242']},
        {'code': '3890352', 'name': 'Software Testing and Quality Assurance', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': []},
        {'code': '3890333', 'name': 'Software Architecture and Design Patterns', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': []},
        {'code': '3590213', 'name': 'Creative Nonfiction', 'metu': '3(3-1)', 'ects': 3.0, 'sem': 6, 'prerequisites': ['3590101', '3590102']},
        {'code': '3550435', 'name': 'Data Communications and Networking', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 7, 'prerequisites': []},
        {'code': '3550400', 'name': 'Summer Practice II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 7, 'prerequisites': ['3870301']},
        {'code': '3890460', 'name': 'Software Security', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7, 'prerequisites': ['3550334']},
        {'code': '3890491', 'name': 'Software Engineering Senior Project I', 'metu': '3(2-2)', 'ects': 7.0, 'sem': 7, 'prerequisites': ['3890303', '3890341']},
        {'code': '3890404', 'name': 'Software Process Management', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7, 'prerequisites': []},
        {'code': '3590219', 'name': 'English Through Seminars On Films', 'metu': '3(3-1)', 'ects': 3.0, 'sem': 7, 'prerequisites': ['3590101', '3590102']},
        {'code': '3890492', 'name': 'Software Engineering Senior Project II', 'metu': '3(1-4)', 'ects': 7.0, 'sem': 8, 'prerequisites': ['3890491']},
        {'code': '3890471', 'name': 'Software Verification and Validation', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8, 'prerequisites': []},
        {'code': '3890420', 'name': 'Software Modeling and Analysis', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8, 'prerequisites': []},
        {'code': '3890457', 'name': 'Software Configuration', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8, 'prerequisites': []},
        {'code': '3660286', 'name': 'Language and society', 'metu': '3(3-0)', 'ects': 4.5, 'sem': 8, 'prerequisites': []},
        {'code': '3760360', 'name': 'Introduction to Visual Design', 'metu': '3(2-2)', 'ects': 4.0, 'sem': 8, 'prerequisites': []},
    ],
    2: [
        {'code': '3570119', 'name': 'Calculus with Analytic Geometry', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 1, 'prerequisites': ['3570100']},
        {'code': '3580105', 'name': 'General Physics I', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 1, 'prerequisites': []},
        {'code': '3550101', 'name': 'Comp. Engineering Orientation', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1, 'prerequisites': []},
        {'code': '3890111', 'name': 'Introduction to Comp. Engineering Concepts', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 1, 'prerequisites': []},
        {'code': '3600107', 'name': 'General Chemistry', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3590101', 'name': 'Development of Reading and Writing Skills I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3550100', 'name': 'Introduction to Computer Science and Programming', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1, 'prerequisites': []},
        {'code': '3530100', 'name': 'Career Planning', 'metu': '0(1-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570120', 'name': 'Calculus for Functions of Several Variables', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 2, 'prerequisites': ['3570119']},
        {'code': '3580106', 'name': 'General Physics II', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 2, 'prerequisites': []},
        {'code': '3890140', 'name': 'Programming', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570260', 'name': 'Basic Linear Algebra', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 2, 'prerequisites': []},
        {'code': '3590102', 'name': 'Development of Reading and Writing Skills II', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 2, 'prerequisites': ['3590101']},
        {'code': '3870101', 'name': 'Occupational Health and Safety-I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570219', 'name': 'Introduction to Differential Equations', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 3, 'prerequisites': ['3570120']},
        {'code': '3890201', 'name': 'Introduction To Software Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 3, 'prerequisites': []},
        {'code': '3550213', 'name': 'Data Structures', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 3, 'prerequisites': ['3890140']},
        {'code': '3550223', 'name': 'Discrete Computational Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 3, 'prerequisites': []},
        {'code': '3590211', 'name': 'Academic Oral Presentation Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 3, 'prerequisites': ['3590102']},
        {'code': '3610101', 'name': 'Turkish I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},
        {'code': '3620201', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},
        {'code': '3630221', 'name': 'Statistics for Engineers I', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4, 'prerequisites': ['3570120']},
        {'code': '3890242', 'name': 'Object Oriented Software Development', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4, 'prerequisites': ['3550213', '3890111']},
        {'code': '3550280', 'name': 'Formal Languages and Abstract Machines', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 4, 'prerequisites': ['3550223']},
        {'code': '3550232', 'name': 'Logic Design', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4, 'prerequisites': []},
        {'code': '3610102', 'name': 'Turkish II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4, 'prerequisites': ['3610101']},
        {'code': '3620202', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4, 'prerequisites': ['3620201']},
        {'code': '3890221', 'name': 'Software Requirements Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4, 'prerequisites': ['3890201']},
        {'code': '3550315', 'name': 'Algorithms', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5, 'prerequisites': ['3550213']},
        {'code': '3550331', 'name': 'Computer Organization', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5, 'prerequisites': ['3550232']},
        {'code': '3550351', 'name': 'Data Management and File Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5, 'prerequisites': []},
        {'code': '3590311', 'name': 'Advanced Communication Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 5, 'prerequisites': ['3590211']},
        {'code': '3890303', 'name': 'Software Project Management', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5, 'prerequisites': []},
        {'code': '3890330', 'name': 'Software Desing', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5, 'prerequisites': ['3890201', '3890242']},
        {'code': '3890300', 'name': 'Summer Practice I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5, 'prerequisites': ['3550100', '3870101']},
        {'code': '3870301', 'name': 'Occupational Health And Safesty II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5, 'prerequisites': []},
        {'code': '3550334', 'name': 'Introduction to Operating Systems', 'metu': '3(3-0)', 'ects': 5.5, 'sem': 6, 'prerequisites': ['3550331']},
        {'code': '3890341', 'name': 'Software Construction and Evolution', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 6, 'prerequisites': ['3890330']},
        {'code': '3890346', 'name': 'Web Aplication Development', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': ['3890242']},
        {'code': '3890352', 'name': 'Software Testing and Quality Assurance', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': []},
        {'code': '3890333', 'name': 'Software Architecture and Design Patterns', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': []},
        {'code': '3690201', 'name': 'Basic German I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 6, 'prerequisites': ['3590101', '3590102']},
        {'code': '3550435', 'name': 'Data Communications and Networking', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 7, 'prerequisites': []},
        {'code': '3550400', 'name': 'Summer Practice II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 7, 'prerequisites': []},
        {'code': '3890460', 'name': 'Software Security', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7, 'prerequisites': ['3550334']},
        {'code': '3890491', 'name': 'Software Engineering Senior Project I', 'metu': '3(2-2)', 'ects': 7.0, 'sem': 7, 'prerequisites': ['3890303', '3890341']},
        {'code': '3890494', 'name': 'Model Driven Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7, 'prerequisites': []},
        {'code': '3690202', 'name': 'Basic German II', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 7, 'prerequisites': ['3690201']},
        {'code': '3890492', 'name': 'Software Engineering Senior Project II', 'metu': '3(1-4)', 'ects': 7.0, 'sem': 8, 'prerequisites': ['3890491']},
        {'code': '3890480', 'name': 'Formal Methods in Specification and Design', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8, 'prerequisites': []},
        {'code': '3890420', 'name': 'Software Modeling and Analysis', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8, 'prerequisites': []},
        {'code': '3890457', 'name': 'Software Configuration', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8, 'prerequisites': []},
        {'code': '3690203', 'name': 'Intermediate German I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 8, 'prerequisites': ['3690202']},
        {'code': '3530447', 'name': 'Intermediate Accounting', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 8, 'prerequisites': []},
    ],
    3: [
        {'code': '3570119', 'name': 'Calculus with Analytic Geometry', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 1, 'prerequisites': ['3570100']},
        {'code': '3580105', 'name': 'General Physics I', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 1, 'prerequisites': []},
        {'code': '3550101', 'name': 'Comp. Engineering Orientation', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1, 'prerequisites': []},
        {'code': '3890111', 'name': 'Introduction to Comp. Engineering Concepts', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 1, 'prerequisites': []},
        {'code': '3600107', 'name': 'General Chemistry', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3590101', 'name': 'Development of Reading and Writing Skills I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3550100', 'name': 'Introduction to Computer Science and Programming', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1, 'prerequisites': []},
        {'code': '3530100', 'name': 'Career Planning', 'metu': '0(1-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570120', 'name': 'Calculus for Functions of Several Variables', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 2, 'prerequisites': ['3570119']},
        {'code': '3580106', 'name': 'General Physics II', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 2, 'prerequisites': []},
        {'code': '3890140', 'name': 'Programming', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570260', 'name': 'Basic Linear Algebra', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 2, 'prerequisites': []},
        {'code': '3590102', 'name': 'Development of Reading and Writing Skills II', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 2, 'prerequisites': ['3590101']},
        {'code': '3870101', 'name': 'Occupational Health and Safety-I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570219', 'name': 'Introduction to Differential Equations', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 3, 'prerequisites': ['3570120']},
        {'code': '3890201', 'name': 'Introduction To Software Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 3, 'prerequisites': []},
        {'code': '3550213', 'name': 'Data Structures', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 3, 'prerequisites': ['3890140']},
        {'code': '3550223', 'name': 'Discrete Computational Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 3, 'prerequisites': []},
        {'code': '3590211', 'name': 'Academic Oral Presentation Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 3, 'prerequisites': ['3590102']},
        {'code': '3610101', 'name': 'Turkish I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},
        {'code': '3620201', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},
        {'code': '3630221', 'name': 'Statistics for Engineers I', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4, 'prerequisites': ['3570120']},
        {'code': '3890242', 'name': 'Object Oriented Software Development', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4, 'prerequisites': ['3550213', '3890111']},
        {'code': '3550280', 'name': 'Formal Languages and Abstract Machines', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 4, 'prerequisites': ['3550223']},
        {'code': '3550232', 'name': 'Logic Design', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4, 'prerequisites': []},
        {'code': '3610102', 'name': 'Turkish II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4, 'prerequisites': ['3610101']},
        {'code': '3620202', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4, 'prerequisites': ['3620201']},
        {'code': '3890221', 'name': 'Software Requirements Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4, 'prerequisites': ['3890201']},
        {'code': '3550315', 'name': 'Algorithms', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5, 'prerequisites': ['3550213']},
        {'code': '3550331', 'name': 'Computer Organization', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5, 'prerequisites': ['3550232']},
        {'code': '3550351', 'name': 'Data Management and File Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5, 'prerequisites': []},
        {'code': '3590311', 'name': 'Advanced Communication Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 5, 'prerequisites': ['3590211']},
        {'code': '3890303', 'name': 'Software Project Management', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5, 'prerequisites': []},
        {'code': '3890330', 'name': 'Software Desing', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5, 'prerequisites': ['3890201', '3890242']},
        {'code': '3890300', 'name': 'Summer Practice I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5, 'prerequisites': ['3550100', '3870101']},
        {'code': '3870301', 'name': 'Occupational Health And Safesty II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5, 'prerequisites': []},
        {'code': '3550334', 'name': 'Introduction to Operating Systems', 'metu': '3(3-0)', 'ects': 5.5, 'sem': 6, 'prerequisites': ['3550331']},
        {'code': '3890341', 'name': 'Software Construction and Evolution', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 6, 'prerequisites': ['3890330']},
        {'code': '3890346', 'name': 'Web Aplication Development', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': ['3890242']},
        {'code': '3890352', 'name': 'Software Testing and Quality Assurance', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': []},
        {'code': '3890404', 'name': 'Software Process Management', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': []},
        {'code': '3760360', 'name': 'Introduction to Visual Design', 'metu': '3(2-2)', 'ects': 4.0, 'sem': 6, 'prerequisites': []},
        {'code': '3550435', 'name': 'Data Communications and Networking', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 7, 'prerequisites': []},
        {'code': '3550400', 'name': 'Summer Practice II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 7, 'prerequisites': ['3870301']},
        {'code': '3890460', 'name': 'Software Security', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7, 'prerequisites': ['3550334']},
        {'code': '3890491', 'name': 'Software Engineering Senior Project I', 'metu': '3(2-2)', 'ects': 7.0, 'sem': 7, 'prerequisites': ['3890303', '3890341']},
        {'code': '3890494', 'name': 'Model Driven Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7, 'prerequisites': []},
        {'code': '3690201', 'name': 'Basic German I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 7, 'prerequisites': ['3590101', '3590102']},
        {'code': '3890492', 'name': 'Software Engineering Senior Project II', 'metu': '3(1-4)', 'ects': 7.0, 'sem': 8, 'prerequisites': ['3890491']},
        {'code': '3890482', 'name': 'Software Measurement and Metrics', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8, 'prerequisites': []},
        {'code': '3890420', 'name': 'Software Modeling and Analysis', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8,'prerequisites': []},
        {'code': '3890457', 'name': 'Software Configuration', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8,'prerequisites': []},
        {'code': '3690202', 'name': 'Basic German II', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 8,'prerequisites': ['3660271','3690201']},
        {'code': '3530447', 'name': 'Intermediate Accounting', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 8,'prerequisites': []},

    ]
}
EEE_CURRICULA_DATA = {
    1: [
        # Version 1 - Semester 1
        {'code': '3570119', 'name': 'Calculus with Analytic Geometry', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 1, 'prerequisites': ['3570100']},
        {'code': '3580105', 'name': 'General Physics I', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 1, 'prerequisites': []},
        {'code': '3600107', 'name': 'General Chemistry', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3560100', 'name': 'Introduction to Electrical and Electronics Engineering', 'metu': '0(1-0)', 'ects': 1.0, 'sem': 1, 'prerequisites': []},
        {'code': '3590101', 'name': 'Development of Reading and Writing Skills I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3550100', 'name': 'Introduction to Information Technologies and Applications', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1, 'prerequisites': []},

        # Version 1 - Semester 2
        {'code': '3530100', 'name': 'Career Planning', 'metu': '0(1-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570120', 'name': 'Calculus for Functions of Several Variables', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 2, 'prerequisites': ['3570119']},
        {'code': '3580106', 'name': 'General Physics II', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 2, 'prerequisites': []},
        {'code': '3550230', 'name': 'Introduction to C Programming', 'metu': '3(2-2)', 'ects': 5.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570260', 'name': 'Basic Linear Algebra', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 2, 'prerequisites': []},
        {'code': '3590102', 'name': 'Development of Reading and Writing Skills II', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 2, 'prerequisites': ['3590101']},
        {'code': '3870101', 'name': 'Occupational Health and Safety-I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},

        # Version 1 - Semester 3
        {'code': '3570219', 'name': 'Differential Equations', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 3, 'prerequisites': ['3570120']},
        {'code': '3560201', 'name': 'Circuits Theory I', 'metu': '5(4-2)', 'ects': 8.0, 'sem': 3, 'prerequisites': ['3570119']},
        {'code': '3650203', 'name': 'Thermodynamics', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 3, 'prerequisites': []},
        {'code': '3550301', 'name': 'Algorithms and Data Structures', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 3, 'prerequisites': ['3550230']},
        {'code': '3590211', 'name': 'Academic Oral Presentation Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 3, 'prerequisites': ['3590101', '3590102']},
        {'code': '3610101', 'name': 'Turkish I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},
        {'code': '3870301', 'name': 'Occupational Health And Safety II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},

        # Version 1 - Semester 4
        {'code': '3560224', 'name': 'Electromagnetic Theory', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 4, 'prerequisites': ['3570120', '3580106']},
        {'code': '3560202', 'name': 'Circuits Theory II', 'metu': '5(4-2)', 'ects': 8.0, 'sem': 4, 'prerequisites': ['3560201', '3570219']},
        {'code': '3560212', 'name': 'Semiconductor Devices and Modeling', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4, 'prerequisites': ['3560201']},
        {'code': '3520101', 'name': 'Microeconomics', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 4, 'prerequisites': []},
        {'code': '3560248', 'name': 'Logic Design', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4, 'prerequisites': []},
        {'code': '3610102', 'name': 'Turkish II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4, 'prerequisites': ['3610101']},

        # Version 1 - Semester 5
        {'code': '3560361', 'name': 'Electromechanical Energy Conversion', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 5, 'prerequisites': ['3560202', '3560224']},
        {'code': '3560303', 'name': 'Electromagnetic Waves', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5, 'prerequisites': ['3560224']},
        {'code': '3560301', 'name': 'Signals and Systems I', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5, 'prerequisites': ['3570219']},
        {'code': '3560311', 'name': 'Electronics I', 'metu': '4(3-2)', 'ects': 8.0, 'sem': 5, 'prerequisites': ['3560202', '3560212']},
        {'code': '3590311', 'name': 'Advanced Communication Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 5, 'prerequisites': ['3590101', '3590102', '3590211']},
        {'code': '3620201', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 5, 'prerequisites': []},
        {'code': '3560300', 'name': 'Summer Practice I', 'metu': '0(0-0)', 'ects': 1.0, 'sem': 5, 'prerequisites': ['3550100', '3560100', '3560202', '3870101']},

        # Version 1 - Semester 6
        {'code': '3560347', 'name': 'Introduction to Microprocessors', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 6, 'prerequisites': ['3560248']},
        {'code': '3560302', 'name': 'Feedback Systems', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': ['3560301']},
        {'code': '3560312', 'name': 'Electronics II', 'metu': '4(3-2)', 'ects': 8.0, 'sem': 6, 'prerequisites': ['3560212']},
        {'code': '3560330', 'name': 'Probability and Random Variables', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': ['3570120']},
        {'code': '3620202', 'name': 'Principles of Kemal Atatürk II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 6, 'prerequisites': ['3620201']},
        {'code': '3690201', 'name': 'Basic German I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 6, 'prerequisites': ['3590101', '3590102']},

        # Version 1 - Semester 7
        {'code': '3560493', 'name': 'Engineering Design I', 'metu': '2(1-2)', 'ects': 7.0, 'sem': 7, 'prerequisites': ['3560302', '3560311', '3560361']},
        {'code': '3560306', 'name': 'Signals and Systems II', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7, 'prerequisites': []},
        {'code': '3560281', 'name': 'Electrical Circuits', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 7, 'prerequisites': ['3570119', '3580106']},
        {'code': '3560209', 'name': 'Fundamentals of Electrical and Electronics Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7, 'prerequisites': ['3580106']},
        {'code': '3690202', 'name': 'Basic German II', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 7, 'prerequisites': ['3690201']},
        {'code': '3560400', 'name': 'Summer Practice II', 'metu': '0(0-0)', 'ects': 1.0, 'sem': 7, 'prerequisites': ['3550100', '3560311', '3870301']},

        # Version 1 - Semester 8
        {'code': '3560494', 'name': 'Engineering Design II', 'metu': '2(1-2)', 'ects': 7.0, 'sem': 8, 'prerequisites': ['3560493']},
        {'code': '3560426', 'name': 'Antennas and Propagation', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 8, 'prerequisites': ['3560224']},
        {'code': '3560404', 'name': 'Nonlinear Control Systems', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8, 'prerequisites': ['3560302']},
        {'code': '3560282', 'name': 'Introduction to Digital Electronics', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 8, 'prerequisites': ['3560281']},
        {'code': '3690203', 'name': 'Intermediate German I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 8, 'prerequisites': ['3690202']},
    ],

    2: [
        # Version 2 - Semester 1 (same as Version 1)
        {'code': '3570119', 'name': 'Calculus with Analytic Geometry', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 1, 'prerequisites': ['3570100']},
        {'code': '3580105', 'name': 'General Physics I', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 1, 'prerequisites': []},
        {'code': '3600107', 'name': 'General Chemistry', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3560100', 'name': 'Introduction to Electrical and Electronics Engineering', 'metu': '0(1-0)', 'ects': 1.0, 'sem': 1, 'prerequisites': []},
        {'code': '3590101', 'name': 'Development of Reading and Writing Skills I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3550100', 'name': 'Introduction to Information Technologies and Applications', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1, 'prerequisites': []},

        # Version 2 - Semester 2 (same as Version 1)
        {'code': '3530100', 'name': 'Career Planning', 'metu': '0(1-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570120', 'name': 'Calculus for Functions of Several Variables', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 2, 'prerequisites': ['3570119']},
        {'code': '3580106', 'name': 'General Physics II', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 2, 'prerequisites': []},
        {'code': '3550230', 'name': 'Introduction to C Programming', 'metu': '3(2-2)', 'ects': 5.0, 'sem': 2, 'prerequisites': []},
        {'code': '3590102', 'name': 'Development of Reading and Writing Skills II', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 2, 'prerequisites': ['3590101']},
        {'code': '3870101', 'name': 'Occupational Health and Safety-I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},

        # Version 2 - Semester 3
        {'code': '3570219', 'name': 'Differential Equations', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 3, 'prerequisites': ['3570120']},
        {'code': '3560201', 'name': 'Circuits Theory I', 'metu': '5(4-2)', 'ects': 8.0, 'sem': 3, 'prerequisites': ['3570119']},
        {'code': '3650203', 'name': 'Thermodynamics', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 3, 'prerequisites': []},
        {'code': '3650113', 'name': 'Computer Aided Engineering Drawing I', 'metu': '3(2-2)', 'ects': 4.5, 'sem': 3, 'prerequisites': []},
        {'code': '3590211', 'name': 'Academic Oral Presentation Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 3, 'prerequisites': ['3590101', '3590102']},
        {'code': '3610101', 'name': 'Turkish I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},
        {'code': '3870301', 'name': 'Occupational Health And Safety II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},

        # Version 2 - Semester 4 (same as Version 1)
        {'code': '3560224', 'name': 'Electromagnetic Theory', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 4, 'prerequisites': ['3570120', '3580106']},
        {'code': '3560202', 'name': 'Circuits Theory II', 'metu': '5(4-2)', 'ects': 8.0, 'sem': 4, 'prerequisites': ['3560201', '3570219']},
        {'code': '3560212', 'name': 'Semiconductor Devices and Modeling', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4, 'prerequisites': ['3560201']},
        {'code': '3520101', 'name': 'Microeconomics', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 4, 'prerequisites': []},
        {'code': '3560248', 'name': 'Logic Design', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4, 'prerequisites': []},
        {'code': '3610102', 'name': 'Turkish II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4, 'prerequisites': ['3610101']},

        # Version 2 - Semester 5
        {'code': '3560361', 'name': 'Electromechanical Energy Conversion', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 5, 'prerequisites': ['3560202', '3560224']},
        {'code': '3520102', 'name': 'Macroeconomics', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 5, 'prerequisites': ['3520101']},
        {'code': '3560301', 'name': 'Signals and Systems I', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5, 'prerequisites': ['3570219']},
        {'code': '3560311', 'name': 'Electronics I', 'metu': '4(3-2)', 'ects': 8.0, 'sem': 5, 'prerequisites': ['3560202', '3560212']},
        {'code': '3590311', 'name': 'Advanced Communication Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 5, 'prerequisites': ['3590101', '3590102', '3590211']},
        {'code': '3620201', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 5, 'prerequisites': []},
        {'code': '3560300', 'name': 'Summer Practice I', 'metu': '0(0-0)', 'ects': 1.0, 'sem': 5, 'prerequisites': ['3550100', '3560100', '3560202', '3870101']},

        # Version 2 - Semester 6
        {'code': '3560347', 'name': 'Introduction to Microprocessors', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 6, 'prerequisites': ['3560248']},
        {'code': '3560302', 'name': 'Feedback Systems', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': ['3560301']},
        {'code': '3650114', 'name': 'Computer Aided Engineering Drawing II', 'metu': '3(2-2)', 'ects': 8.0, 'sem': 6, 'prerequisites': ['3560113']},
        {'code': '3630221', 'name': 'Statistics for Engineers I', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': ['3570120']},
        {'code': '3620202', 'name': 'Principles of Kemal Atatürk II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 6, 'prerequisites': ['3620201']},
        {'code': '3690201', 'name': 'Basic German I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 6, 'prerequisites': ['3590101', '3590102']},

        # Version 2 - Semester 7
        {'code': '3560493', 'name': 'Engineering Design I', 'metu': '2(1-2)', 'ects': 7.0, 'sem': 7, 'prerequisites': ['3560302', '3560311', '3560361']},
        {'code': '3650405', 'name': 'Energy Conversion Systems', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7, 'prerequisites': []},
        {'code': '3560281', 'name': 'Electrical Circuits', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 7, 'prerequisites': ['3570119', '3580106']},
        {'code': '3560441', 'name': 'Data Structures', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7, 'prerequisites': ['3550230']},
        {'code': '3690202', 'name': 'Basic German II', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 7, 'prerequisites': ['3690201']},
        {'code': '3560400', 'name': 'Summer Practice II', 'metu': '0(0-0)', 'ects': 1.0, 'sem': 7, 'prerequisites': ['3550100', '3560311', '3870301']},

        # Version 2 - Semester 8
        {'code': '3560494', 'name': 'Engineering Design II', 'metu': '2(1-2)', 'ects': 7.0, 'sem': 8, 'prerequisites': ['3560493']},
        {'code': '3560445', 'name': 'Computer Architecture', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8, 'prerequisites': ['3560248']},
        {'code': '3560404', 'name': 'Nonlinear Control Systems', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8, 'prerequisites': ['3560302']},
        {'code': '3560463', 'name': 'Static Power Conversion', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 8, 'prerequisites': ['3560212']},
        {'code': '3690203', 'name': 'Intermediate German I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 8, 'prerequisites': ['3690202']},
    ],

    3: [
        # Version 3 - Semester 1 (same as Versions 1 and 2)
        {'code': '3570119', 'name': 'Calculus with Analytic Geometry', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 1, 'prerequisites': ['3570100']},
        {'code': '3580105', 'name': 'General Physics I', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 1, 'prerequisites': []},
        {'code': '3600107', 'name': 'General Chemistry', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3560100', 'name': 'Introduction to Electrical and Electronics Engineering', 'metu': '0(1-0)', 'ects': 1.0, 'sem': 1, 'prerequisites': []},
        {'code': '3590101', 'name': 'Development of Reading and Writing Skills I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3550100', 'name': 'Introduction to Information Technologies and Applications', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1, 'prerequisites': []},

        # Version 3 - Semester 2 (same as Versions 1 and 2)
        {'code': '3530100', 'name': 'Career Planning', 'metu': '0(1-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570120', 'name': 'Calculus for Functions of Several Variables', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 2, 'prerequisites': ['3570119']},
        {'code': '3580106', 'name': 'General Physics II', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 2, 'prerequisites': []},
        {'code': '3550230', 'name': 'Introduction to C Programming', 'metu': '3(2-2)', 'ects': 5.0, 'sem': 2, 'prerequisites': []},
        {'code': '3590102', 'name': 'Development of Reading and Writing Skills II', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 2, 'prerequisites': ['3590101']},
        {'code': '3870101', 'name': 'Occupational Health and Safety-I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},

        # Version 3 - Semester 3
        {'code': '3570219', 'name': 'Differential Equations', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 3, 'prerequisites': ['3570120']},
        {'code': '3560201', 'name': 'Circuits Theory I', 'metu': '5(4-2)', 'ects': 8.0, 'sem': 3, 'prerequisites': ['3570119']},
        {'code': '3550223', 'name': 'Discrete Computational Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 3, 'prerequisites': []},
        {'code': '3650113', 'name': 'Computer Aided Engineering Drawing I', 'metu': '3(2-2)', 'ects': 4.5, 'sem': 3, 'prerequisites': []},
        {'code': '3590211', 'name': 'Academic Oral Presentation Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 3, 'prerequisites': ['3590101', '3590102']},
        {'code': '3610101', 'name': 'Turkish I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},
        {'code': '3870301', 'name': 'Occupational Health And Safety II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},

        # Version 3 - Semester 4
        {'code': '3560224', 'name': 'Electromagnetic Theory', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 4, 'prerequisites': ['3570120', '3580106']},
        {'code': '3560202', 'name': 'Circuits Theory II', 'metu': '5(4-2)', 'ects': 8.0, 'sem': 4, 'prerequisites': ['3560201', '3570219']},
        {'code': '3560212', 'name': 'Semiconductor Devices and Modeling', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4, 'prerequisites': ['3560201']},
        {'code': '3520101', 'name': 'Microeconomics', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 4, 'prerequisites': []},
        {'code': '3560248', 'name': 'Logic Design', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4, 'prerequisites': []},
        {'code': '3610102', 'name': 'Turkish II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4, 'prerequisites': ['3610101']},
        {'code': '3550280', 'name': 'Formal Languages and Abstract Machines', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 4, 'prerequisites': ['3550223']},

        # Version 3 - Semester 5 (same as Version 2)
        {'code': '3560361', 'name': 'Electromechanical Energy Conversion', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 5, 'prerequisites': ['3560202', '3560224']},
        {'code': '3520102', 'name': 'Macroeconomics', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 5, 'prerequisites': ['3520101']},
        {'code': '3560301', 'name': 'Signals and Systems I', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5, 'prerequisites': ['3570219']},
        {'code': '3560311', 'name': 'Electronics I', 'metu': '4(3-2)', 'ects': 8.0, 'sem': 5, 'prerequisites': ['3560202', '3560212']},
        {'code': '3590311', 'name': 'Advanced Communication Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 5, 'prerequisites': ['3590101', '3590102', '3590211']},
        {'code': '3620201', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 5, 'prerequisites': []},
        {'code': '3560300', 'name': 'Summer Practice I', 'metu': '0(0-0)', 'ects': 1.0, 'sem': 5, 'prerequisites': ['3550100', '3560100', '3560202', '3870101']},

        # Version 3 - Semester 6
        {'code': '3550315', 'name': 'Algorithms', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 6, 'prerequisites': ['3550230']},
        {'code': '3560302', 'name': 'Feedback Systems', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': ['3560301']},
        {'code': '3550316', 'name': 'Practice of Algorithms', 'metu': '3(2-0)', 'ects': 6.0, 'sem': 6, 'prerequisites': ['3550230']},
        {'code': '3630221', 'name': 'Statistics for Engineers I', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6, 'prerequisites': ['3570120']},
        {'code': '3620202', 'name': 'Principles of Kemal Atatürk II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 6, 'prerequisites': ['3620201']},
        {'code': '3690201', 'name': 'Basic German I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 6, 'prerequisites': ['3590101', '3590102']},

        # Version 3 - Semester 7
        {'code': '3560493', 'name': 'Engineering Design I', 'metu': '2(1-2)', 'ects': 7.0, 'sem': 7, 'prerequisites': ['3560302', '3560311', '3560361']},
        {'code': '3550435', 'name': 'Data Communications and Computer Networking', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 7, 'prerequisites': []},
        {'code': '3560281', 'name': 'Electrical Circuits', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 7, 'prerequisites': ['3570119', '3580106']},
        {'code': '3560441', 'name': 'Data Structures', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7, 'prerequisites': ['3550230']},
        {'code': '3690202', 'name': 'Basic German II', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 7, 'prerequisites': ['3690201']},
        {'code': '3560400', 'name': 'Summer Practice II', 'metu': '0(0-0)', 'ects': 1.0, 'sem': 7, 'prerequisites': ['3550100', '3560311', '3870301']},

        # Version 3 - Semester 8 (same as Version 2)
        {'code': '3560494', 'name': 'Engineering Design II', 'metu': '2(1-2)', 'ects': 7.0, 'sem': 8, 'prerequisites': ['3560493']},
        {'code': '3560445', 'name': 'Computer Architecture', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8, 'prerequisites': ['3560248']},
        {'code': '3560404', 'name': 'Nonlinear Control Systems', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8, 'prerequisites': ['3560302']},
        {'code': '3560463', 'name': 'Static Power Conversion', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 8,'prerequisites': ['3560212']},
        {'code': '3690203', 'name': 'Intermediate German I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 8,'prerequisites': ['3690202']},
    ]
}

CNG_CURRICULA_DATA = {
    1: [
        # 1st Semester
        {'code': '3570119', 'name': 'Calculus with Analytic Geometry', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 1,
         'prerequisites': ['3570100']},
        {'code': '3580105', 'name': 'General Physics I', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 1, 'prerequisites': []},
        {'code': '3550101', 'name': 'Comp. Engineering Orientation', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1,
         'prerequisites': []},
        {'code': '3550111', 'name': 'Introduction to Comp. Engineering Concepts', 'metu': '4(3-2)', 'ects': 4.0,
         'sem': 1, 'prerequisites': []},
        {'code': '3600107', 'name': 'General Chemistry', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3590101', 'name': 'Development of Reading and Writing Skills I', 'metu': '4(4-0)', 'ects': 6.0,
         'sem': 1, 'prerequisites': []},
        {'code': '3550100', 'name': 'Introduction to Information Technologies and Applications', 'metu': '0(2-0)',
         'ects': 1.0, 'sem': 1, 'prerequisites': []},

        # 2nd Semester
        {'code': '3530100', 'name': 'Career Planning', 'metu': '0(1-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570120', 'name': 'Calculus for Functions of Several Variables', 'metu': '5(4-2)', 'ects': 7.5,
         'sem': 2, 'prerequisites': ['3570119']},
        {'code': '3580106', 'name': 'General Physics II', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 2, 'prerequisites': []},
        {'code': '3550140', 'name': 'C Programming', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570260', 'name': 'Basic Linear Algebra', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 2,
         'prerequisites': []},
        {'code': '3590102', 'name': 'Development of Reading and Writing Skills II', 'metu': '4(4-0)', 'ects': 6.0,
         'sem': 2, 'prerequisites': ['3590101']},
        {'code': '3870101', 'name': 'Occupational Health and Safety-I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 2,
         'prerequisites': []},

        # 3rd Semester
        {'code': '3570219', 'name': 'Differential Equations', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 3,
         'prerequisites': ['3570120']},
        {'code': '3560281', 'name': 'Electrical Circuits', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 3,
         'prerequisites': ['3570119', '3580106']},
        {'code': '3550213', 'name': 'Data Structures', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 3,
         'prerequisites': ['3550140']},
        {'code': '3550223', 'name': 'Discrete Computational Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 3,
         'prerequisites': []},
        {'code': '3590211', 'name': 'Academic Oral Presentation Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 3,
         'prerequisites': ['3590102']},
        {'code': '3610101', 'name': 'Turkish I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},

        # 4th Semester
        {'code': '3630221', 'name': 'Statistics for Engineers I / Probability and Random Variables', 'metu': '3(3-0)',
         'ects': 5.0, 'sem': 4, 'prerequisites': ['3570120']},
        {'code': '3550242', 'name': 'Programming Language Concepts', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4,
         'prerequisites': ['3550111', '3550213']},
        {'code': '3550280', 'name': 'Formal Languages and Abstract Machines', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 4,
         'prerequisites': ['3550223']},
        {'code': '3550232', 'name': 'Logic Design', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4, 'prerequisites': []},
        {'code': '3610102', 'name': 'Turkish II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4,
         'prerequisites': ['3610101']},
        {'code': '3530447', 'name': 'Intermediate Accounting', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 4,
         'prerequisites': []},

        # 5th Semester
        {'code': '3550315', 'name': 'Algorithms', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5,
         'prerequisites': ['3550213']},
        {'code': '3550331', 'name': 'Computer Organization', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5,
         'prerequisites': ['3550232']},
        {'code': '3550351', 'name': 'Data Management and File Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5,
         'prerequisites': []},
        {'code': '3550462', 'name': 'Wireless Communications and Network', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5,
         'prerequisites': ['3550435']},
        {'code': '3590311', 'name': 'Advanced Communication Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 5,
         'prerequisites': ['3590211']},
        {'code': '3620201', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 5,
         'prerequisites': []},
        {'code': '3550300', 'name': 'Summer Practice I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5,
         'prerequisites': ['3550100', '3870101']},
        {'code': '3870301', 'name': 'Occupational Health And Safesty II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5,
         'prerequisites': []},

        # 6th Semester
        {'code': '3550336', 'name': 'Intro to Embedded Systems / Microprocessors', 'metu': '4(3-2)', 'ects': 5.5,
         'sem': 6, 'prerequisites': ['3550232']},
        {'code': '3550334', 'name': 'Introduction to Operating Systems', 'metu': '3(3-0)', 'ects': 5.5, 'sem': 6,
         'prerequisites': ['3550331']},
        {'code': '3550384', 'name': 'Signals and Systems for Computer Engineers', 'metu': '3(3-0)', 'ects': 5.0,
         'sem': 6, 'prerequisites': ['3570219', '3570260']},
        {'code': '3550350', 'name': 'Software Engineering', 'metu': '3(3-0)', 'ects': 5.5, 'sem': 6,
         'prerequisites': ['3550213']},
        {'code': '3760360', 'name': 'Introduction to Visual Design', 'metu': '3(2-2)', 'ects': 4.0, 'sem': 6,
         'prerequisites': []},
        {'code': '3620202', 'name': 'Principles of Kemal Atatürk II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 6,
         'prerequisites': ['3620201']},

        # 7th Semester
        {'code': '3550491', 'name': 'Senior Project and Seminar: Design', 'metu': '3(2-2)', 'ects': 7.0, 'sem': 7,
         'prerequisites': ['3550350']},
        {'code': '3550435', 'name': 'Data Communications and Networking', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 7,
         'prerequisites': []},
        {'code': '3550477', 'name': 'Practice of Algorithms', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 7,
         'prerequisites': ['3550315']},
        {'code': '3550495', 'name': 'Systems Programming and Support Environments', 'metu': '3(3-0)', 'ects': 5.0,
         'sem': 7, 'prerequisites': ['3550331']},
        {'code': '3540304', 'name': 'English Through Seminars on Films', 'metu': '3(3-0)', 'ects': 8.0, 'sem': 7,
         'prerequisites': []},
        {'code': '3550400', 'name': 'Summer Practice II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 7,
         'prerequisites': ['3870301']},

        # 8th Semester
        {'code': '3550492', 'name': 'Senior Project and Seminar: Implementation', 'metu': '3(1-4)', 'ects': 7.0,
         'sem': 8, 'prerequisites': ['3550491']},
        {'code': '3550436', 'name': 'Software Development with Scripted Languages', 'metu': '3(3-0)', 'ects': 6.0,
         'sem': 8, 'prerequisites': ['3550242']},
        {'code': '3550438', 'name': 'Introduction to Service Oriented Computing', 'metu': '3(3-0)', 'ects': 6.0,
         'sem': 8, 'prerequisites': ['3550455']},
        {'code': '3550353', 'name': 'Scalable Web Application Development', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 8,
         'prerequisites': ['3550351', '3550435']},
        {'code': '3660286', 'name': 'Language and society', 'metu': '3(3-0)', 'ects': 4.5, 'sem': 8,
         'prerequisites': []}
    ],

    2: [
        # 1st Semester (Same as Program 1)
        {'code': '3570119', 'name': 'Calculus with Analytic Geometry', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 1,
         'prerequisites': ['3570100']},
        {'code': '3580105', 'name': 'General Physics I', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 1, 'prerequisites': []},
        {'code': '3550101', 'name': 'Comp. Engineering Orientation', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1,
         'prerequisites': []},
        {'code': '3550111', 'name': 'Introduction to Comp. Engineering Concepts', 'metu': '4(3-2)', 'ects': 4.0,
         'sem': 1, 'prerequisites': []},
        {'code': '3600107', 'name': 'General Chemistry', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3590101', 'name': 'Development of Reading and Writing Skills I', 'metu': '4(4-0)', 'ects': 6.0,
         'sem': 1, 'prerequisites': []},
        {'code': '3550100', 'name': 'Introduction to Information Technologies and Applications', 'metu': '0(2-0)',
         'ects': 1.0, 'sem': 1, 'prerequisites': []},

        # 2nd Semester (Same as Program 1)
        {'code': '3530100', 'name': 'Career Planning', 'metu': '0(1-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570120', 'name': 'Calculus for Functions of Several Variables', 'metu': '5(4-2)', 'ects': 7.5,
         'sem': 2, 'prerequisites': ['3570119']},
        {'code': '3580106', 'name': 'General Physics II', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 2, 'prerequisites': []},
        {'code': '3550140', 'name': 'C Programming', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570260', 'name': 'Basic Linear Algebra', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 2,
         'prerequisites': []},
        {'code': '3590102', 'name': 'Development of Reading and Writing Skills II', 'metu': '4(4-0)', 'ects': 6.0,
         'sem': 2, 'prerequisites': ['3590101']},
        {'code': '3870101', 'name': 'Occupational Health and Safety-I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 2,
         'prerequisites': []},

        # 3rd Semester (Same as Program 1)
        {'code': '3570219', 'name': 'Differential Equations', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 3,
         'prerequisites': ['3570120']},
        {'code': '3560281', 'name': 'Electrical Circuits', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 3,
         'prerequisites': ['3570119', '3580106']},
        {'code': '3550213', 'name': 'Data Structures', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 3,
         'prerequisites': ['3550140']},
        {'code': '3550223', 'name': 'Discrete Computational Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 3,
         'prerequisites': []},
        {'code': '3590211', 'name': 'Academic Oral Presentation Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 3,
         'prerequisites': ['3590102']},
        {'code': '3610101', 'name': 'Turkish I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},

        # 4th Semester (Same as Program 1)
        {'code': '3630221', 'name': 'Statistics for Engineers I / Probability and Random Variables', 'metu': '3(3-0)',
         'ects': 5.0, 'sem': 4, 'prerequisites': ['3570120']},
        {'code': '3550242', 'name': 'Programming Language Concepts', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4,
         'prerequisites': ['3550111', '3550213']},
        {'code': '3550280', 'name': 'Formal Languages and Abstract Machines', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 4,
         'prerequisites': ['3550223']},
        {'code': '3550232', 'name': 'Logic Design', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4, 'prerequisites': []},
        {'code': '3610102', 'name': 'Turkish II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4,
         'prerequisites': ['3610101']},
        {'code': '3530447', 'name': 'Intermediate Accounting', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 4,
         'prerequisites': []},

        # 5th Semester (Different in Program 2)
        {'code': '3550315', 'name': 'Algorithms', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5,
         'prerequisites': ['3550213']},
        {'code': '3550331', 'name': 'Computer Organization', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5,
         'prerequisites': ['3550232']},
        {'code': '3550351', 'name': 'Data Management and File Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5,
         'prerequisites': []},
        {'code': '3550462', 'name': 'Artificial Intelligence', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5,
         'prerequisites': []},  # Changed from Wireless Comm
        {'code': '3590311', 'name': 'Advanced Communication Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 5,
         'prerequisites': ['3590211']},
        {'code': '3620201', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 5,
         'prerequisites': []},
        {'code': '3550300', 'name': 'Summer Practice I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5,
         'prerequisites': ['3550100', '3870101']},
        {'code': '3870301', 'name': 'Occupational Health And Safesty II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5,
         'prerequisites': []},

        # 6th Semester (Same as Program 1)
        {'code': '3550336', 'name': 'Intro to Embedded Systems / Microprocessors', 'metu': '4(3-2)', 'ects': 5.5,
         'sem': 6, 'prerequisites': ['3550232']},
        {'code': '3550334', 'name': 'Introduction to Operating Systems', 'metu': '3(3-0)', 'ects': 5.5, 'sem': 6,
         'prerequisites': ['3550331']},
        {'code': '3550384', 'name': 'Signals and Systems for Computer Engineers', 'metu': '3(3-0)', 'ects': 5.0,
         'sem': 6, 'prerequisites': ['3570219', '3570260']},
        {'code': '3550350', 'name': 'Software Engineering', 'metu': '3(3-0)', 'ects': 5.5, 'sem': 6,
         'prerequisites': ['3550213']},
        {'code': '3760360', 'name': 'Introduction to Visual Design', 'metu': '3(2-2)', 'ects': 4.0, 'sem': 6,
         'prerequisites': []},
        {'code': '3620202', 'name': 'Principles of Kemal Atatürk II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 6,
         'prerequisites': ['3620201']},

        # 7th Semester (Different in Program 2)
        {'code': '3550491', 'name': 'Senior Project and Seminar: Design', 'metu': '3(2-2)', 'ects': 7.0, 'sem': 7,
         'prerequisites': ['3550350']},
        {'code': '3550435', 'name': 'Data Communications and Networking', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 7,
         'prerequisites': []},
        {'code': '3550477', 'name': 'Introduction to Computer Graphics', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 7,
         'prerequisites': ['3550213']},  # Changed from Practice of Algorithms
        {'code': '3550495', 'name': 'Cloud Computing', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7,
         'prerequisites': ['3550331', '3550351']},  # Changed from Systems Programming
        {'code': '3540304', 'name': 'International Organizations', 'metu': '3(3-0)', 'ects': 8.0, 'sem': 7,
         'prerequisites': []},  # Changed from English Through Films
        {'code': '3550400', 'name': 'Summer Practice II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 7,
         'prerequisites': ['3870301']},

        # 8th Semester (Different in Program 2)
        {'code': '3550492', 'name': 'Senior Project and Seminar: Implementation', 'metu': '3(1-4)', 'ects': 7.0,
         'sem': 8, 'prerequisites': ['3550491']},
        {'code': '3550436', 'name': 'Wireless Communications and Network', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 8,
         'prerequisites': ['3550435']},  # Changed from Scripted Languages
        {'code': '3550438', 'name': 'Introduction to Service Oriented Computing', 'metu': '3(3-0)', 'ects': 6.0,
         'sem': 8, 'prerequisites': ['3550334', '3550435']},  # Changed prerequisites
        {'code': '3550353', 'name': 'Scalable Web Application Development', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 8,
         'prerequisites': []},  # No prerequisites
        {'code': '3660286', 'name': 'Language and Society', 'metu': '3(3-0)', 'ects': 4.5, 'sem': 8,
         'prerequisites': []}
    ],

    3: [
        # 1st Semester (Same as Program 1)
        {'code': '3570119', 'name': 'Calculus with Analytic Geometry', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 1,
         'prerequisites': ['3570100']},
        {'code': '3580105', 'name': 'General Physics I', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 1, 'prerequisites': []},
        {'code': '3550101', 'name': 'Comp. Engineering Orientation', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1,
         'prerequisites': []},
        {'code': '3550111', 'name': 'Introduction to Comp. Engineering Concepts', 'metu': '4(3-2)', 'ects': 4.0,
         'sem': 1, 'prerequisites': []},
        {'code': '3600107', 'name': 'General Chemistry', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 1, 'prerequisites': []},
        {'code': '3590101', 'name': 'Development of Reading and Writing Skills I', 'metu': '4(4-0)', 'ects': 6.0,
         'sem': 1, 'prerequisites': []},
        {'code': '3550100', 'name': 'Introduction to Information Technologies and Applications', 'metu': '0(2-0)',
         'ects': 1.0, 'sem': 1, 'prerequisites': []},

        # 2nd Semester (Same as Program 1)
        {'code': '3530100', 'name': 'Career Planning', 'metu': '0(1-0)', 'ects': 2.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570120', 'name': 'Calculus for Functions of Several Variables', 'metu': '5(4-2)', 'ects': 7.5,
         'sem': 2, 'prerequisites': ['3570119']},
        {'code': '3580106', 'name': 'General Physics II', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 2, 'prerequisites': []},
        {'code': '3550140', 'name': 'C Programming', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 2, 'prerequisites': []},
        {'code': '3570260', 'name': 'Basic Linear Algebra', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 2,
         'prerequisites': []},
        {'code': '3590102', 'name': 'Development of Reading and Writing Skills II', 'metu': '4(4-0)', 'ects': 6.0,
         'sem': 2, 'prerequisites': ['3590101']},
        {'code': '3870101', 'name': 'Occupational Health and Safety-I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 2,
         'prerequisites': []},

        # 3rd Semester (Same as Program 1)
        {'code': '3570219', 'name': 'Differential Equations', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 3,
         'prerequisites': ['3570120']},
        {'code': '3560281', 'name': 'Electrical Circuits', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 3,
         'prerequisites': ['3570119', '3580106']},
        {'code': '3550213', 'name': 'Data Structures', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 3,
         'prerequisites': ['3550140']},
        {'code': '3550223', 'name': 'Discrete Computational Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 3,
         'prerequisites': []},
        {'code': '3590211', 'name': 'Academic Oral Presentation Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 3,
         'prerequisites': ['3590102']},
        {'code': '3610101', 'name': 'Turkish I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3, 'prerequisites': []},

        # 4th Semester (Same as Program 1)
        {'code': '3630221', 'name': 'Statistics for Engineers I / Probability and Random Variables', 'metu': '3(3-0)',
         'ects': 5.0, 'sem': 4, 'prerequisites': ['3570120']},
        {'code': '3550242', 'name': 'Programming Language Concepts', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4,
         'prerequisites': ['3550111', '3550213']},
        {'code': '3550280', 'name': 'Formal Languages and Abstract Machines', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 4,
         'prerequisites': ['3550223']},
        {'code': '3550232', 'name': 'Logic Design', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4, 'prerequisites': []},
        {'code': '3610102', 'name': 'Turkish II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4,
         'prerequisites': ['3610101']},
        {'code': '3530447', 'name': 'Intermediate Accounting', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 4,
         'prerequisites': []},

        # 5th Semester (Different in Program 3)
        {'code': '3550315', 'name': 'Algorithms', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5,
         'prerequisites': ['3550213']},
        {'code': '3550331', 'name': 'Computer Organization', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5,
         'prerequisites': ['3550232']},
        {'code': '3550351', 'name': 'Data Management and File Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5,
         'prerequisites': []},
        {'code': '3550436', 'name': 'Wireless Communications and Network', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5,
         'prerequisites': ['3550435']},  # Moved from 8th sem
        {'code': '3590311', 'name': 'Advanced Communication Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 5,
         'prerequisites': ['3590211']},
        {'code': '3620201', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 5,
         'prerequisites': []},
        {'code': '3550300', 'name': 'Summer Practice I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5,
         'prerequisites': ['3550100', '3870101']},
        {'code': '3870301', 'name': 'Occupational Health And Safesty II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5,
         'prerequisites': []},

        # 6th Semester (Same as Program 1)
        {'code': '3550336', 'name': 'Intro to Embedded Systems / Microprocessors', 'metu': '4(3-2)', 'ects': 5.5,
         'sem': 6, 'prerequisites': ['3550232']},
        {'code': '3550334', 'name': 'Introduction to Operating Systems', 'metu': '3(3-0)', 'ects': 5.5, 'sem': 6,
         'prerequisites': ['3550331']},
        {'code': '3550384', 'name': 'Signals and Systems for Computer Engineers', 'metu': '3(3-0)', 'ects': 5.0,
         'sem': 6, 'prerequisites': ['3570219', '3570260']},
        {'code': '3550350', 'name': 'Software Engineering', 'metu': '3(3-0)', 'ects': 5.5, 'sem': 6,
         'prerequisites': ['3550213']},
        {'code': '3760360', 'name': 'Introduction to Visual Design', 'metu': '3(2-2)', 'ects': 4.0, 'sem': 6,
         'prerequisites': []},
        {'code': '3620202', 'name': 'Principles of Kemal Atatürk II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 6,
         'prerequisites': ['3620201']},

        # 7th Semester (Different in Program 3)
        {'code': '3550491', 'name': 'Senior Project and Seminar: Design', 'metu': '3(2-2)', 'ects': 7.0, 'sem': 7,
         'prerequisites': ['3550350']},
        {'code': '3550435', 'name': 'Data Communications and Networking', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 7,
         'prerequisites': []},
        {'code': '3550316', 'name': 'Practice of Algorithms', 'metu': '3(2-2)', 'ects': 6.0, 'sem': 7,
         'prerequisites': ['3550315']},  # Different code and format
        {'code': '3550332', 'name': 'Systems Programming and Support Environments', 'metu': '3(3-0)', 'ects': 6.0,
         'sem': 7, 'prerequisites': ['3550331']},  # Different code
        {'code': '3540304', 'name': 'International Organizations', 'metu': '3(3-0)', 'ects': 8.0, 'sem': 7,
         'prerequisites': []},  # Same as Program 2
        {'code': '3550400', 'name': 'Summer Practice II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 7,
         'prerequisites': ['3870301']},

        # 8th Semester (Different in Program 3)
        {'code': '3550492', 'name': 'Senior Project and Seminar: Implementation', 'metu': '3(1-4)', 'ects': 7.0,
         'sem': 8, 'prerequisites': ['3550491']},
        {'code': '3550445', 'name': 'Software Development with Scripting Languages', 'metu': '3(3-0)', 'ects': 6.0,
         'sem': 8, 'prerequisites': ['3550242']},
        {'code': '3550455', 'name': 'Introduction to Service Oriented Computing', 'metu': '3(3-0)', 'ects': 6.0,
         'sem': 8, 'prerequisites': ['3550455']},
        {'code': '3550456', 'name': 'Scalable Web Application Development', 'metu': '3(3-0)', 'ects': 6.0,
         'sem': 8, 'prerequisites': ['3550351','3550435']},
        {'code': '3660286', 'name': 'Language and society', 'metu': '3(3-0)', 'ects': 4.5,
         'sem': 8, 'prerequisites': []},
]
}
    
def populate_sample_data(self):
        """
        Populates the database using all three curriculum datasets.
        """
        print("--- Starting Sample Data Population ---")

        # 1. Add Departments
        departments_data = [
            ("CNG", "Computer Engineering"),
            ("EEE", "Electrical & Electronics Engineering"),
            ("SNG", "Software Engineering")
        ]
        print("1. Adding departments...")
        for dept_id, dept_name in departments_data:
            self.add_department(dept_id, dept_name)
        print("   Departments processed.")

        # 2. Populate curricula from all embedded datasets
        all_curriculum_ids = {"CNG": [], "EEE": [], "SNG": []}
        curricula_datasets = {
            "CNG": CNG_CURRICULA_DATA,
            "EEE": EEE_CURRICULA_DATA,
            "SNG": SNG_CURRICULA_DATA
        }

        print("\n2. Populating curricula from embedded data...")
        for dept_id, curriculum_data in curricula_datasets.items():
            print(f"  Processing {dept_id} curricula...")
            for version_num, courses in curriculum_data.items():
                print(f"    Processing version {version_num}...")
                version_name = f"{dept_id} Curriculum v{version_num} (Embedded)"
                curriculum_id = self.add_curriculum_version(dept_id, version_num, version_name)

                if curriculum_id:
                    courses_added_count = 0
                    for course_data in courses:
                        self.add_course_name(course_data['code'], course_data['name'], dept_id)
                        if self.add_course_to_curriculum(
                                curriculum_id,
                                course_data['code'],
                                course_data['metu'],
                                course_data['ects'],
                                semester_suggested=course_data['sem']
                        ):
                            courses_added_count += 1
                    print(f"      -> Added {courses_added_count} courses to curriculum ID {curriculum_id}.")
                    all_curriculum_ids[dept_id].append(curriculum_id)
                else:
                    print(f"    Failed to create curriculum version {version_num} for {dept_id}.")

        # 3. Add Students and Enrollments
        print("\n3. Adding students and their enrollments...")
        student_counter = 1
        grades = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF", "EX", "P", "NA"]
        semesters = ["2021-Fall", "2022-Spring", "2022-Fall", "2023-Spring", "2023-Fall", "2024-Spring"]
        first_names = ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Elif", "Cem", "Deniz", "Emir", "Selin"]
        last_names = ["Yilmaz", "Kaya", "Demir", "Şahin", "Çelik", "Yildiz", "Özdemir", "Arslan", "Koç", "Aydin"]

        for dept_id, dept_name in departments_data:
            print(f"  Populating 25 students for department: {dept_name}")
            for _ in range(25):
                student_id = f"26{str(student_counter).zfill(5)}"
                first_name = random.choice(first_names)
                last_name = random.choice(last_names)

                # Assign curriculum based on department
                assigned_curriculum_id = None
                if all_curriculum_ids[dept_id]:
                    assigned_curriculum_id = random.choice(all_curriculum_ids[dept_id])
                else:
                    # Create placeholder curriculum if none exists
                    assigned_curriculum_id = self.add_curriculum_version(
                        dept_id, 1, f"{dept_name} Placeholder Curriculum"
                    )

                if assigned_curriculum_id is None:
                    student_counter += 1
                    continue

                if self.add_student(student_id, first_name, last_name, dept_id, assigned_curriculum_id):
                    # Get courses for this curriculum
                    conn_temp = self.get_connection()
                    c_temp = conn_temp.cursor()
                    c_temp.execute(
                        "SELECT course_code FROM curriculum_courses WHERE curriculum_id = ?",
                        (assigned_curriculum_id,)
                    )
                    courses_in_curriculum = [row[0] for row in c_temp.fetchall()]
                    conn_temp.close()

                    if courses_in_curriculum:
                        # Randomly enroll student in some courses
                        num_enrollments = random.randint(
                            max(1, len(courses_in_curriculum) // 2),
                            len(courses_in_curriculum)
                        )
                        courses_to_enroll_in = random.sample(courses_in_curriculum, num_enrollments)

                        for course_code in courses_to_enroll_in:
                            self.add_enrollment(
                                student_id,
                                course_code,
                                random.choice(semesters),
                                random.choice(grades)
                            )

                student_counter += 1

        print(f"\nProcessed {student_counter - 1} student profiles.")
        print("--- Sample Data Population Completed ---")


if __name__ == "__main__":
    db_file_name = "transcript_system.db"

    # Remove existing database for fresh start
    if os.path.exists(db_file_name):
        print(f"Removing existing database: {db_file_name} for a fresh run.")
        os.remove(db_file_name)

    # Create database instance and populate with sample data
    db = TranscriptDatabase(db_name=db_file_name)
    db.populate_sample_data()  # Fixed: call method on the instance

    print("\n=== Database Test Queries ===")
    all_students = db.get_all_students()
    print(f"Total students found in DB: {len(all_students)}")

    if all_students:
        # Test with first 5 students
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