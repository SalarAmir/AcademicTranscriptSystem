# curriculum_data.py

"""
This file contains the embedded curriculum data for the SNG department.
It is imported by database.py to populate the curriculum tables.
"""

SNG_CURRICULA_DATA = {
    1: [
        {'code': '3570119', 'name': 'Calculus with Analytic Geometry', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 1},
        {'code': '3580105', 'name': 'General Physics I', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 1},
        {'code': '3550101', 'name': 'Comp. Engineering Orientation', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1},
        {'code': '3890111', 'name': 'Introduction to Comp. Engineering Concepts', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 1},
        {'code': '3600107', 'name': 'General Chemistry', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 1},
        {'code': '3590101', 'name': 'Development of Reading and Writing Skills I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 1},
        {'code': '3550100', 'name': 'Introduction to Computer Science and Programming', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1},
        {'code': '3530100', 'name': 'Career Planning', 'metu': '0(1-0)', 'ects': 2.0, 'sem': 2},
        {'code': '3570120', 'name': 'Calculus for Functions of Several Variables', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 2},
        {'code': '3580106', 'name': 'General Physics II', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 2},
        {'code': '3890140', 'name': 'Programming', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 2},
        {'code': '3570260', 'name': 'Basic Linear Algebra', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 2},
        {'code': '3590102', 'name': 'Development of Reading and Writing Skills II', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 2},
        {'code': '3870101', 'name': 'Occupational Health and Safety-I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 2},
        {'code': '3570219', 'name': 'Introduction to Differential Equations', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 3},
        {'code': '3890201', 'name': 'Introduction To Software Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 3},
        {'code': '3550213', 'name': 'Data Structures', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 3},
        {'code': '3550223', 'name': 'Discrete Computational Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 3},
        {'code': '3590211', 'name': 'Academic Oral Presentation Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 3},
        {'code': '3610101', 'name': 'Turkish I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3},
        {'code': '3620201', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3},
        {'code': '3630221', 'name': 'Statistics for Engineers I', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4},
        {'code': '3890242', 'name': 'Object Oriented Software Development', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4},
        {'code': '3550280', 'name': 'Formal Languages and Abstract Machines', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 4},
        {'code': '3550232', 'name': 'Logic Design', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4},
        {'code': '3610102', 'name': 'Turkish II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4},
        {'code': '3620202', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4},
        {'code': '3890221', 'name': 'Software Requirements Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4},
        {'code': '3550315', 'name': 'Algorithms', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5},
        {'code': '3550331', 'name': 'Computer Organization', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5},
        {'code': '3550351', 'name': 'Data Management and File Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5},
        {'code': '3590311', 'name': 'Advanced Communication Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 5},
        {'code': '3890303', 'name': 'Software Project Management', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5},
        {'code': '3890330', 'name': 'Software Desing', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5},
        {'code': '3890300', 'name': 'Summer Practice I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5},
        {'code': '3870301', 'name': 'Occupational Health And Safesty II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5},
        {'code': '3550334', 'name': 'Introduction to Operating Systems', 'metu': '3(3-0)', 'ects': 5.5, 'sem': 6},
        {'code': '3890341', 'name': 'Software Construction and Evolution', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 6},
        {'code': '3890346', 'name': 'Web Aplication Development', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6},
        {'code': '3890352', 'name': 'Software Testing and Quality Assurance', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6},
        {'code': '3890333', 'name': 'Software Architecture and Design Patterns', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6},
        {'code': '3590213', 'name': 'Creative Nonfiction', 'metu': '3(3-1)', 'ects': 3.0, 'sem': 6},
        {'code': '3550435', 'name': 'Data Communications and Networking', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 7},
        {'code': '3550400', 'name': 'Summer Practice II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 7},
        {'code': '3890460', 'name': 'Software Security', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7},
        {'code': '3890491', 'name': 'Software Engineering Senior Project I', 'metu': '3(2-2)', 'ects': 7.0, 'sem': 7},
        {'code': '3890404', 'name': 'Software Process Management', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7},
        {'code': '3590219', 'name': 'English Through Seminars On Films', 'metu': '3(3-1)', 'ects': 3.0, 'sem': 7},
        {'code': '3890492', 'name': 'Software Engineering Senior Project II', 'metu': '3(1-4)', 'ects': 7.0, 'sem': 8},
        {'code': '3890471', 'name': 'Software Verification and Validation', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8},
        {'code': '3890420', 'name': 'Software Modeling and Analysis', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8},
        {'code': '3890457', 'name': 'Software Configuration', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8},
        {'code': '3660286', 'name': 'Language and society', 'metu': '3(3-0)', 'ects': 4.5, 'sem': 8},
        {'code': '3760360', 'name': 'Introduction to Visual Design', 'metu': '3(2-2)', 'ects': 4.0, 'sem': 8},
    ],
    2: [
        {'code': '3570119', 'name': 'Calculus with Analytic Geometry', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 1},
        {'code': '3580105', 'name': 'General Physics I', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 1},
        {'code': '3550101', 'name': 'Comp. Engineering Orientation', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1},
        {'code': '3890111', 'name': 'Introduction to Comp. Engineering Concepts', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 1},
        {'code': '3600107', 'name': 'General Chemistry', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 1},
        {'code': '3590101', 'name': 'Development of Reading and Writing Skills I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 1},
        {'code': '3550100', 'name': 'Introduction to Computer Science and Programming', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1},
        {'code': '3530100', 'name': 'Career Planning', 'metu': '0(1-0)', 'ects': 2.0, 'sem': 2},
        {'code': '3570120', 'name': 'Calculus for Functions of Several Variables', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 2},
        {'code': '3580106', 'name': 'General Physics II', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 2},
        {'code': '3890140', 'name': 'Programming', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 2},
        {'code': '3570260', 'name': 'Basic Linear Algebra', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 2},
        {'code': '3590102', 'name': 'Development of Reading and Writing Skills II', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 2},
        {'code': '3870101', 'name': 'Occupational Health and Safety-I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 2},
        {'code': '3570219', 'name': 'Introduction to Differential Equations', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 3},
        {'code': '3890201', 'name': 'Introduction To Software Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 3},
        {'code': '3550213', 'name': 'Data Structures', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 3},
        {'code': '3550223', 'name': 'Discrete Computational Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 3},
        {'code': '3590211', 'name': 'Academic Oral Presentation Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 3},
        {'code': '3610101', 'name': 'Turkish I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3},
        {'code': '3620201', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3},
        {'code': '3630221', 'name': 'Statistics for Engineers I', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4},
        {'code': '3890242', 'name': 'Object Oriented Software Development', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4},
        {'code': '3550280', 'name': 'Formal Languages and Abstract Machines', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 4},
        {'code': '3550232', 'name': 'Logic Design', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4},
        {'code': '3610102', 'name': 'Turkish II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4},
        {'code': '3620202', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4},
        {'code': '3890221', 'name': 'Software Requirements Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4},
        {'code': '3550315', 'name': 'Algorithms', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5},
        {'code': '3550331', 'name': 'Computer Organization', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5},
        {'code': '3550351', 'name': 'Data Management and File Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5},
        {'code': '3590311', 'name': 'Advanced Communication Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 5},
        {'code': '3890303', 'name': 'Software Project Management', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5},
        {'code': '3890330', 'name': 'Software Desing', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5},
        {'code': '3890300', 'name': 'Summer Practice I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5},
        {'code': '3870301', 'name': 'Occupational Health And Safesty II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5},
        {'code': '3550334', 'name': 'Introduction to Operating Systems', 'metu': '3(3-0)', 'ects': 5.5, 'sem': 6},
        {'code': '3890341', 'name': 'Software Construction and Evolution', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 6},
        {'code': '3890346', 'name': 'Web Aplication Development', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6},
        {'code': '3890352', 'name': 'Software Testing and Quality Assurance', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6},
        {'code': '3890333', 'name': 'Software Architecture and Design Patterns', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6},
        {'code': '3690201', 'name': 'Basic German I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 6},
        {'code': '3550435', 'name': 'Data Communications and Networking', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 7},
        {'code': '3550400', 'name': 'Summer Practice II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 7},
        {'code': '3890460', 'name': 'Software Security', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7},
        {'code': '3890491', 'name': 'Software Engineering Senior Project I', 'metu': '3(2-2)', 'ects': 7.0, 'sem': 7},
        {'code': '3890494', 'name': 'Model Driven Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7},
        {'code': '3690202', 'name': 'Basic German II', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 7},
        {'code': '3890492', 'name': 'Software Engineering Senior Project II', 'metu': '3(1-4)', 'ects': 7.0, 'sem': 8},
        {'code': '3890480', 'name': 'Formal Methods in Specification and Design', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8},
        {'code': '3890420', 'name': 'Software Modeling and Analysis', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8},
        {'code': '3890457', 'name': 'Software Configuration', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8},
        {'code': '3690203', 'name': 'Intermediate German I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 8},
        {'code': '3530447', 'name': 'Intermediate Accounting', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 8},
    ],
    3: [
        {'code': '3570119', 'name': 'Calculus with Analytic Geometry', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 1},
        {'code': '3580105', 'name': 'General Physics I', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 1},
        {'code': '3550101', 'name': 'Comp. Engineering Orientation', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1},
        {'code': '3890111', 'name': 'Introduction to Comp. Engineering Concepts', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 1},
        {'code': '3600107', 'name': 'General Chemistry', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 1},
        {'code': '3590101', 'name': 'Development of Reading and Writing Skills I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 1},
        {'code': '3550100', 'name': 'Introduction to Computer Science and Programming', 'metu': '0(2-0)', 'ects': 1.0, 'sem': 1},
        {'code': '3530100', 'name': 'Career Planning', 'metu': '0(1-0)', 'ects': 2.0, 'sem': 2},
        {'code': '3570120', 'name': 'Calculus for Functions of Several Variables', 'metu': '5(4-2)', 'ects': 7.5, 'sem': 2},
        {'code': '3580106', 'name': 'General Physics II', 'metu': '4(3-2)', 'ects': 6.5, 'sem': 2},
        {'code': '3890140', 'name': 'Programming', 'metu': '4(3-2)', 'ects': 4.0, 'sem': 2},
        {'code': '3570260', 'name': 'Basic Linear Algebra', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 2},
        {'code': '3590102', 'name': 'Development of Reading and Writing Skills II', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 2},
        {'code': '3870101', 'name': 'Occupational Health and Safety-I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 2},
        {'code': '3570219', 'name': 'Introduction to Differential Equations', 'metu': '4(4-0)', 'ects': 7.0, 'sem': 3},
        {'code': '3890201', 'name': 'Introduction To Software Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 3},
        {'code': '3550213', 'name': 'Data Structures', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 3},
        {'code': '3550223', 'name': 'Discrete Computational Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 3},
        {'code': '3590211', 'name': 'Academic Oral Presentation Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 3},
        {'code': '3610101', 'name': 'Turkish I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3},
        {'code': '3620201', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 3},
        {'code': '3630221', 'name': 'Statistics for Engineers I', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4},
        {'code': '3890242', 'name': 'Object Oriented Software Development', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4},
        {'code': '3550280', 'name': 'Formal Languages and Abstract Machines', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 4},
        {'code': '3550232', 'name': 'Logic Design', 'metu': '4(3-2)', 'ects': 7.0, 'sem': 4},
        {'code': '3610102', 'name': 'Turkish II', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4},
        {'code': '3620202', 'name': 'Principles of Kemal Atatürk I', 'metu': '0(2-0)', 'ects': 2.0, 'sem': 4},
        {'code': '3890221', 'name': 'Software Requirements Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 4},
        {'code': '3550315', 'name': 'Algorithms', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5},
        {'code': '3550331', 'name': 'Computer Organization', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5},
        {'code': '3550351', 'name': 'Data Management and File Structures', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 5},
        {'code': '3590311', 'name': 'Advanced Communication Skills', 'metu': '3(3-0)', 'ects': 4.0, 'sem': 5},
        {'code': '3890303', 'name': 'Software Project Management', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5},
        {'code': '3890330', 'name': 'Software Desing', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 5},
        {'code': '3890300', 'name': 'Summer Practice I', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5},
        {'code': '3870301', 'name': 'Occupational Health And Safesty II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 5},
        {'code': '3550334', 'name': 'Introduction to Operating Systems', 'metu': '3(3-0)', 'ects': 5.5, 'sem': 6},
        {'code': '3890341', 'name': 'Software Construction and Evolution', 'metu': '4(3-2)', 'ects': 6.0, 'sem': 6},
        {'code': '3890346', 'name': 'Web Aplication Development', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6},
        {'code': '3890352', 'name': 'Software Testing and Quality Assurance', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6},
        {'code': '3890404', 'name': 'Software Process Management', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 6},
        {'code': '3760360', 'name': 'Introduction to Visual Design', 'metu': '3(2-2)', 'ects': 4.0, 'sem': 6},
        {'code': '3550435', 'name': 'Data Communications and Networking', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 7},
        {'code': '3550400', 'name': 'Summer Practice II', 'metu': '0(0-0)', 'ects': 2.0, 'sem': 7},
        {'code': '3890460', 'name': 'Software Security', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7},
        {'code': '3890491', 'name': 'Software Engineering Senior Project I', 'metu': '3(2-2)', 'ects': 7.0, 'sem': 7},
        {'code': '3890494', 'name': 'Model Driven Engineering', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 7},
        {'code': '3690201', 'name': 'Basic German I', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 7},
        {'code': '3890492', 'name': 'Software Engineering Senior Project II', 'metu': '3(1-4)', 'ects': 7.0, 'sem': 8},
        {'code': '3890482', 'name': 'Software Measurement and Metrics', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8},
        {'code': '3890420', 'name': 'Software Modeling and Analysis', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8},
        {'code': '3890457', 'name': 'Software Configuration', 'metu': '3(3-0)', 'ects': 5.0, 'sem': 8},
        {'code': '3690202', 'name': 'Basic German II', 'metu': '4(4-0)', 'ects': 6.0, 'sem': 8},
        {'code': '3530447', 'name': 'Intermediate Accounting', 'metu': '3(3-0)', 'ects': 6.0, 'sem': 8},
    ]
}

def populate_sample_data(self):
        """
        Populates the database using the embedded SNG curriculum data.
        """
        print("--- Starting Sample Data Population ---")
        
        # 1. Add Departments
        departments_data = [("SNG", "Software Engineering"), ("CSE", "Computer Science & Engineering"), ("EEE", "Electrical & Electronics Engineering")]
        print("1. Adding departments...")
        for dept_id, dept_name in departments_data:
            self.add_department(dept_id, dept_name)
        print("   Departments processed.")

        # 2. Populate SNG Curricula from the embedded data
        sng_curriculum_ids = []
        print("\n2. Populating SNG curriculum from embedded data...")
        for version_num, courses in self.SNG_CURRICULA_DATA.items():
            print(f"  Processing version {version_num}...")
            version_name = f"SNG Curriculum v{version_num} (Embedded)"
            curriculum_id = self.add_curriculum_version("SNG", version_num, version_name)
            
            if curriculum_id:
                courses_added_count = 0
                for course_data in courses:
                    self.add_course_name(course_data['code'], course_data['name'], "SNG")
                    if self.add_course_to_curriculum(curriculum_id, course_data['code'], course_data['metu'], course_data['ects'], semester_suggested=course_data['sem']):
                        courses_added_count += 1
                print(f"    -> Added {courses_added_count} courses to curriculum ID {curriculum_id}.")
                sng_curriculum_ids.append(curriculum_id)
            else:
                print(f"  Failed to create curriculum version {version_num}.")
        
        # 3. Add Students and Enrollments
        print("\n3. Adding students and their enrollments...")
        student_counter = 1
        grades = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FF", "EX", "P", "NA"]
        semesters = ["2021-Fall", "2022-Spring", "2022-Fall", "2023-Spring", "2023-Fall", "2024-Spring"]
        first_names = ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Elif", "Cem", "Deniz", "Emir", "Selin"]
        last_names = ["Yilmaz", "Kaya", "Demir", "Şahin", "Çelik", "Yildiz", "Özdemir", "Arslan", "Koç", "Aydin"]

        for dept_id_loop, dept_name_loop in departments_data:
            print(f"  Populating 25 students for department: {dept_name_loop}")
            for _ in range(25):
                student_id = f"26{str(student_counter).zfill(5)}"
                first_name = random.choice(first_names)
                last_name = random.choice(last_names)
                
                assigned_curriculum_id = None
                
                if dept_id_loop == "SNG" and sng_curriculum_ids:
                    assigned_curriculum_id = random.choice(sng_curriculum_ids)
                else:
                    assigned_curriculum_id = self.add_curriculum_version(dept_id_loop, 1, f"{dept_name_loop} Placeholder Curriculum")
                
                if assigned_curriculum_id is None:
                     student_counter += 1; continue

                if self.add_student(student_id, first_name, last_name, dept_id_loop, assigned_curriculum_id):
                    conn_temp = self.get_connection()
                    c_temp = conn_temp.cursor()
                    c_temp.execute("SELECT course_code FROM curriculum_courses WHERE curriculum_id = ?", (assigned_curriculum_id,))
                    courses_in_curriculum = [row[0] for row in c_temp.fetchall()]
                    conn_temp.close()

                    if courses_in_curriculum:
                        num_enrollments = random.randint(max(1, len(courses_in_curriculum)//2), len(courses_in_curriculum))
                        courses_to_enroll_in = random.sample(courses_in_curriculum, num_enrollments)
                        
                        for course_code in courses_to_enroll_in:
                            self.add_enrollment(student_id, course_code, random.choice(semesters), random.choice(grades))
                
                student_counter += 1
        
        print(f"\nProcessed {student_counter - 1} student profiles.")
        print("--- Sample Data Population Completed ---")


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
