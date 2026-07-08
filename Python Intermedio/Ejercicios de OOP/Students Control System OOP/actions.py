import csv
import re
import data


def add_student():
    while True:
        try:
            n = int(input("How many students do you want to add?: "))
            if n <= 0: 
                print("Please enter a valid number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    for i in range(n):
        print(f"\n--- Student {i+1} ---")
        
        name_validate = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+(?:\s+[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+)+$"
        while True:
            try:
                name = input("Name: ")
                if not re.match(name_validate, name):
                    raise ValueError 
                break
            except ValueError:
                print("Please enter a valid name.")
        while True:
            print("Enter the student's level(Number) and group(Letter)):")
            try:
                level = input("Level: ")
                if not level.isdigit():
                    raise ValueError
                group = input("Group: ")
                if not group.isalpha() or len(group) != 1:
                    raise ValueError
                section = f"{level}{group}"
            except (UnicodeEncodeError, ValueError):
                print("Please enter a valid section.")
            break
        while True:
            try:
                student_id = input("Student ID: ")
                if not len(str(student_id)) == 9:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid student ID.")
        while True:
            try:
                spanish_score = float(input("Spanish Score: "))
                if not 0 <= spanish_score <= 100:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid score between 0 and 100.")
        while True:
            try:
                english_score = float(input("English Score: "))
                if not 0 <= english_score <= 100:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid score between 0 and 100.")
        while True:
            try:
                science_score = float(input("Science Score: "))
                if not 0 <= science_score <= 100:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid score between 0 and 100.")
        while True:
            try:
                social_studies_score = float(input("Social Studies Score: "))
                if not 0 <= social_studies_score <= 100:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid score between 0 and 100.")
        if data.student_exist(student_id, name):
                print("Student already exists.")
                continue
        new_student = data.Student(
            name=name,
            section=section,
            student_id=student_id,
            spanish_score=spanish_score,
            english_score=english_score,
            science_score=science_score,
            social_studies_score=social_studies_score
        )
        data.adding_student(new_student)





def display_students_info():
    list = data.obtaining_students() if hasattr(data, 'obtain_students') else data.obtaining_students()
    if not list:
        print("\nNo students registered currently.\n")
        return
    print("\n================ STUDENT INFORMATION ================")
    
    for student in list:
        print(f"Name: {student.name:<15} | Section: {student.section:<10} | Student ID: {student.student_id}")
        print(f"Spanish: {student.spanish_score} | English: {student.english_score} | Science: {student.science_score} | Social Studies: {student.social_studies_score}")
        print("----------------------------------------------------------------------------")
    print("="*50)   


def modify_record():
    file = data.obtaining_students()
    if not file:
        print("\nNo students registered currently.\n")
        return
    search_id = input("Enter the Student ID of the record you want to modify: ")
    matching_student = [student for student in file if student.student_id == search_id]
    if not matching_student:
        print("\nError: No record found with that ID.")
        return
    matching_student = matching_student[0]
    print(f"\nRecord found: Name: {matching_student.name} - Section: {matching_student.section} - Student ID: {matching_student.student_id}")
    print("\nEnter the NEW data (leave blank to keep the current value):")
    fields = [
        ('name', 'Name'),
        ('section', 'Section'),
        ('spanish_score', 'Spanish Score'),
        ('english_score', 'English Score'),
        ('science_score', 'Science Score'),
        ('social_studies_score', 'Social Studies Score')
    ]
    for attribute, tag in fields:
        current_value = getattr(matching_student, attribute)
        new_value = input(f"{tag} (Current: {current_value}): ")
        if new_value.strip():
            setattr(matching_student, attribute, new_value)
    
    original_index = file.index(matching_student)
    data.update_student(
        original_index,
        matching_student.name,
        matching_student.section,
        matching_student.spanish_score,
        matching_student.english_score,
        matching_student.science_score,
        matching_student.social_studies_score
    )
    print("\nSuccess: Record updated successfully!")
    


def delete_students():
    info = data.obtaining_students() 
    if not info:
        print("\nNo students registered currently.\n")
        return
    search_name = input("Input the name of the student: ").strip().lower()
    search_section = input("Input the section of the student: ").strip().lower()
    matching_students = [student for student in info if search_name in student.name.lower() and search_section == student.section.lower()]
    if not matching_students:
        print("\n[!] Error: No student found with that name and section.")
        return
    student_to_delete = matching_students[0]
    print(f"\nStudent found: {student_to_delete.name} - Section: {student_to_delete.section} - Student ID: {student_to_delete.student_id}")
    confirmation = input("Are you sure you want to delete this student? (y/n): ").strip().lower()
    if confirmation == 'y':
        if student_to_delete in info:
            info.remove(student_to_delete)
            print("\n[+] Successfully deleted the student.")
        else:print("\nError: Could not delete the record.")
    else:
        print("\n[-] Operation cancelled. No changes were made.")


def calculate_average(students_list):
    if not students_list:
        print("\nNo students registered currently.\n")
        return
    try:
        print(f"{'Student Name':<20} | {'Average'}")
        print("-" * 32)
            
        for student in students_list:
            name = student.name
            spanish_score = student.spanish_score
            english_score = student.english_score
            science_score = student.science_score
            social_studies_score = student.social_studies_score

            average = (spanish_score + english_score + science_score + social_studies_score) / 4
            print(f"{name:<20} | {average:.2f}")
            print("-" * 32)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    print("="*32)


def show_top3():
    file = data.obtaining_students()
    if not file:
        print("\nNo students registered currently.\n")
        return
    students_averages = []
    try:
        for student in file:
            name = student.name
            spanish_score = student.spanish_score
            english_score = student.english_score
            science_score = student.science_score
            social_studies_score = student.social_studies_score

            average = (spanish_score + english_score + science_score + social_studies_score) / 4
            students_averages.append((name, average))
            students_averages.sort(key=lambda x: x[1], reverse=True)
        print("\nTop 3 Students:")
        print(f"{'Position':<8} | {'Student Name':<20} | {'Average'}")
        print("-" * 43)
        for i, (name, average) in enumerate(students_averages[:3], start=1):
            print(f"#{i:<7} | {name:<20} | {average:.2f}")
        print("-" * 43)
    
    except Exception as e:
        print(f"An error occurred: {e}")


def display_failed_students():
    file = data.obtaining_students()
    if not file:
        print("\nNo students registered currently.\n")
        return
    
    print("\n=== FAILED STUDENTS REPORT ===")
    print("="*50)
    has_failed_students = False
        
    for student in file:
            student_name = student.name
            section = student.section
            failed_subjects = []
            for key, value in student.__dict__.items():
                if key in ['name', 'section']:
                    continue
                
                try:
                    grade = float(value)
                    if grade < 60:
                        failed_subjects.append(f"{key} ({grade})")
                except ValueError:
                    continue
            if failed_subjects:
                has_failed_students = True
                print(f"\nStudent:  {student_name}")
                print(f"Section:  {section}")
                print(f"Failed:   {', '.join(failed_subjects)}")
                print("-" * 40)
    if not has_failed_students:
        print("\nGreat news! No students have failed any subjects.")