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
        student = {
            "Name": name,   
            "Section": section,
            "Student ID": student_id,
            "Spanish Score": spanish_score,
            "English Score": english_score, 
            "Science Score": science_score,
            "Social Studies Score": social_studies_score
        }
        data.adding_student(student)





def display_students_info():
    list = data.obtaining_students() if hasattr(data, 'obtain_students') else data.obtaining_students()
    if not list:
        print("\nNo students registered currently.\n")
        return
    print("\n================ STUDENT INFORMATION ================")
    

    for student in list:
        print(f"Name: {student['Name']:<15} | Section: {student['Section']:<10} | Student ID: {student['Student ID']}")
        print(f"Spanish: {student['Spanish Score']} | English: {student['English Score']} | Science: {student['Science Score']} | Social Studies: {student['Social Studies Score']}")
        print("----------------------------------------------------------------------------")
    print("="*50)   


def modify_record():
    info = data.obtaining_students() 
    if not info:
        print("\nNo students registered currently.\n")
        return
    search_id = input("Enter the Student ID of the record you want to modify: ")
    record_found = False

    for e in info:
        if e['Student ID'] == search_id:
            record_found = True
            print(f"\nRecord found: {e}")
            print("\nEnter the NEW data (leave blank to keep the current value):")
            for key in info[0].keys():
                if key == 'Student ID':
                    continue
                current_value = e[key]
                new_value = input(f"{key} (Current: {current_value}): ")
                if new_value.strip():
                    e[key] = new_value
            break

    if record_found:
        data.update_student(info.index(e), e['Name'], e['Section'], e['Student ID'], e['Spanish Score'], e['English Score'], e['Science Score'], e['Social Studies Score'])
        print("\nSuccess: Record updated successfully!")
    else:
        print("\nError: No record found with that ID.")


def delete_students():
    info = data.obtaining_students() 
    if not info:
        print("\nNo students registered currently.\n")
        return
    search_name = input("Input the name of the student: ").strip().lower()
    search_section = input("Input the section of the student: ").strip().lower()
    students = []
    found = False
    student_to_delete = None
    for key in info:
            if key['Name'].strip().lower() == search_name and key['Section'].strip().lower() == search_section:
                found = True
                student_to_delete = key
            else:
                students.append(key)
    if not found:
        print("\n[!] Error: The student does not exist in that section.") 
        return
    print(f"\nStudent found: {student_to_delete['Name']} - Section: {student_to_delete['Section']} - Student ID: {student_to_delete['Student ID']}")
    confirmation = input("Are you sure you want to delete this student? (y/n): ").strip().lower()
    if confirmation == 'y':
        data.students_list.clear()
        data.students_list.extend(students)
        print("\n[+] Successfully deleted the student.")
    else:
        print("\n[-] Operation cancelled. No changes were made.")


def calculate_average():
    file = data.obtaining_students()
    if not file:
        print("\nNo students registered currently.\n")
        return
    try:
        print(f"{'Student':<20} | {'Average'}")
        print("-" * 32)
            
        for e in file:
            name = e['Name']
            spanish_score = e['Spanish Score']
            english_score = e['English Score']
            science_score = e['Science Score']
            social_studies_score = e['Social Studies Score']

            average = ((spanish_score + english_score + science_score + social_studies_score) / 4)
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
        for e in file:
            name = e['Name']
            spanish_score = e['Spanish Score']
            english_score = e['English Score']
            science_score = e['Science Score']
            social_studies_score = e['Social Studies Score']

            average = ((spanish_score + english_score + science_score + social_studies_score) / 4)
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
        
    for e in file:
            student_name = e['Name']
            section = e['Section']
            failed_subjects = []
            for key, value in e.items():
                if key in ['Name', 'Section']:
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