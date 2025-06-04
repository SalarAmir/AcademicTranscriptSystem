# METU NCC Student Transcript Generation System

## Project Overview

This project is a Python-based software system designed to generate academic transcripts for students at a university, specifically tailored to METU Northern Cyprus Campus (NCC) regulations and requirements as per the SNG 242 Semester Project. It utilizes Object-Oriented principles and provides a command-line interface (CLI) for generating transcripts in HTML and PDF formats.

The system manages student data, versioned curricula, course enrollments, and grades, calculating semester GPAs and cumulative CGPAs according to METU NCC's undergraduate education regulations.

## Features

* **Database Management**: Uses SQLite to store student, course, curriculum, and enrollment data.
    * Populates with sample data: 3 departments, 3 curriculum versions per department, and 25 students per department.
    * Supports parsing curriculum specifications from CSV files.
* **Grade Calculation**:
    * Implements METU NCC grade calculation rules (Article 24).
    * Handles repeated courses (last grade counts for CGPA).
    * Excludes 'EX' (Exempt) courses from GPA/CGPA calculations.
* **Transcript Generation**:
    * Generates detailed `TranscriptData` objects for each student.
    * Produces well-formatted transcripts in **HTML** and **PDF**.
* **Command-Line Interface (CLI)**: Allows users to:
    * Generate a transcript for a single student by ID.
    * Generate transcripts for all students in a specific department.
    * Generate transcripts for all students in the university.
    * Choose output format (HTML, PDF, or both).

## Project Structure

The project is organized into the following main Python modules:

* `database.py`: Handles database creation, population, and data access.
* `grade_calculator.py`: Performs all GPA and CGPA calculations.
* `transcript_generator.py`: Orchestrates the data fetching and calculation to produce transcript data objects.
* `transcript_formatter.py`: Formats the transcript data into HTML and PDF documents.
* `main_cli.py`: Provides the command-line interface for user interaction (Note: This script combines functionalities from the other modules for end-user operation).

## Prerequisites

* Python 3.x
* `reportlab` (for PDF generation):
    ```bash
    pip install reportlab
    ```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-name>
    ```
2.  **Install dependencies:**
    ```bash
    pip install reportlab
    ```
3.  **Initialize and Populate the Database:**
    Run the `database.py` script once to create the `transcript_system.db` file and populate it with sample data:
    ```bash
    python database.py
    ```
    This will create the necessary tables and add sample departments, curricula, students, and enrollments.

## Usage

The primary way to use the system is through `main_cli.py`.

**Command-Line Options:**
