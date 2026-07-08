import csv
from operator import index
class Student:
    def __init__(self, name, section, student_id, spanish_score, english_score, science_score, social_studies_score):
        self.name = name
        self.section = section
        self.student_id = student_id
        self.spanish_score = float(spanish_score)
        self.english_score = float(english_score)
        self.science_score = float(science_score)
        self.social_studies_score = float(social_studies_score)
students_list = []

def adding_student(new_student):
    students_list.append(new_student)
    print(f"\nStudents added successfully.\n")


def student_exist(student_id, name):
    file = students_list
    if not file:
        return False
    
    for student in file:
            id_exist= student.student_id == student_id
            name_exists = student.name.strip().lower() == name.strip().lower()
            
            if id_exist:
                return True
            elif name_exists and id_exist:
                return True  
    return False


def obtaining_students():
    return students_list


def update_student(index, name, section, spanish_score, english_score, science_score, social_studies_score):
    students_list[index] = Student(name, section, students_list[index].student_id, spanish_score, english_score, science_score, social_studies_score)


def export_data():
    file = input("Enter the filename to export: ")
    if export_to_csv(file):
        print(f"\nData exported successfully to {file}.\n")
    else:
        print("\nError exporting data.\n")


def import_data():
    file = input("Enter the filename to import: ")
    if import_to_csv(file):
        print(f"\nData imported successfully from {file}.\n")
    else:
        print("\nError importing data (please check if the file exists).\n")


def export_to_csv(path):
    info = obtaining_students()
    fieldnames = ["Name", "Section", "Student ID", "Spanish Score", "English Score", "Social Studies Score", "Science Score"]
    try:
        with open(path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(fieldnames)
            for student in info:
                writer.writerow([
                    student.name, 
                    student.section, 
                    student.student_id, 
                    student.spanish_score, 
                    student.english_score, 
                    student.science_score, 
                    student.social_studies_score
                    ])
        return True
    except Exception:
        return False


def import_to_csv(path):
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                new_student = Student(
                    name=row[0],
                    section=row[1],
                    student_id=row[2],
                    spanish_score=float(row[3]),
                    english_score=float(row[4]),
                    science_score=float(row[5]),
                    social_studies_score=float(row[6])
                )
                adding_student(new_student)
        return True
    except Exception:
        return False