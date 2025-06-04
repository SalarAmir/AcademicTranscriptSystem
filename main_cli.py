# main_cli.py
import argparse
import os
from transcript_generator import TranscriptGenerator, TranscriptData
from transcript_formatter import TranscriptFormatter

def main():
    parser = argparse.ArgumentParser(description="METU NCC Transcript Generation System")
    parser.add_argument("--student_id", help="Generate transcript for a single student ID (e.g., SNG2020001)")
    parser.add_argument("--dept_id", help="Generate transcripts for all students in a department ID (e.g., SNG)")
    parser.add_argument("--all_students", action="store_true", help="Generate transcripts for all students")
    parser.add_argument("--format", choices=['html', 'pdf', 'both'], default='pdf', help="Output format (default: pdf)")
    parser.add_argument("--output_dir", default="transcripts", help="Directory to save transcripts (default: transcripts)")
    parser.add_argument("--db_path", default="transcript_system.db", help="Path to the database file (default: transcript_system.db)")

    args = parser.parse_args()

    # Ensure the database exists.
    if not os.path.exists(args.db_path):
        print(f"Error: Database file '{args.db_path}' not found.")
        print("Please ensure 'database.py' has been run to create and populate the database,")
        print("or specify the correct path using --db_path.")
        return

    generator = TranscriptGenerator(db_path=args.db_path)
    formatter = TranscriptFormatter(output_dir=args.output_dir)
    # ensure_output_directory is called in formatter's __init__

    transcripts_data_to_process: list[TranscriptData] = []

    if args.student_id:
        print(f"Attempting to generate transcript data for student: {args.student_id}")
        data = generator.generate_student_transcript(args.student_id)
        if data:
            transcripts_data_to_process.append(data)
        # generate_student_transcript prints errors/warnings if student/enrollments not found
    elif args.dept_id:
        print(f"Attempting to generate transcript data for department: {args.dept_id}")
        department_data_list = generator.generate_department_transcripts(args.dept_id)
        transcripts_data_to_process.extend(department_data_list)
    elif args.all_students:
        print("Attempting to generate transcript data for all students...")
        all_students_data_list = generator.generate_all_transcripts()
        transcripts_data_to_process.extend(all_students_data_list)
    else:
        parser.print_help()
        return

    if not transcripts_data_to_process:
        print("No students found matching the criteria, or no data to generate transcripts for.")
        return

    generated_files_count = 0
    print(f"\nFound {len(transcripts_data_to_process)} transcript(s) to format.")

    for data_item in transcripts_data_to_process:
        if not isinstance(data_item, TranscriptData):
            print(f"Warning: Expected TranscriptData object, got {type(data_item)}. Skipping.")
            continue

        student_id_for_file = data_item.student_id
        print(f"Processing formatting for student: {student_id_for_file}")

        if args.format == 'html' or args.format == 'both':
            try:
                filepath = formatter.generate_html_transcript(data_item)
                print(f"  Generated HTML transcript: {filepath}")
                generated_files_count += 1
            except Exception as e:
                print(f"  Error generating HTML for {student_id_for_file}: {e}")
        
        if args.format == 'pdf' or args.format == 'both':
            try:
                filepath = formatter.generate_pdf_transcript(data_item)
                if filepath: # generate_pdf_transcript returns None on error
                    print(f"  Generated PDF transcript: {filepath}")
                    generated_files_count += 1
                # else: generate_pdf_transcript prints its own errors
            except Exception as e: # Should ideally be caught within generate_pdf_transcript
                print(f"  Unexpected error during PDF formatting for {student_id_for_file}: {e}")

    if generated_files_count > 0:
        print(f"\nSuccessfully generated {generated_files_count} transcript file(s) in the '{os.path.abspath(args.output_dir)}' directory.")
    else:
        print("\nNo transcript files were generated in this run (check for previous errors or warnings).")

if __name__ == "__main__":
    main()