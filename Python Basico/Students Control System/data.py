import csv

students_list = []

def adding_student(student):
    students_list.append(student)
    print(f"\nStudents added successfully.\n")


def student_exist(student_id, name):
    file = students_list
    if not file:
        return False
    
    for e in file:
            id_exist= e['Student ID'].strip() == student_id.strip()
            name_exists = e['Name'].strip().lower() == name.strip().lower()
            
            if id_exist:
                return True
            elif name_exists and id_exist:
                return True  
    return False


def obtaining_students():
    return students_list


def update_student(index, name, section, student_id, spanish_score, english_score, science_score, social_studies_score):
    students_list[index] = {
        "Name": name,
        "Section": section,
        "Student ID": student_id,
        "Spanish Score": spanish_score,
        "English Score": english_score,
        "Science Score": science_score,
        "Social Studies Score": social_studies_score
    }


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
    try:
        with open(path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Section", "Student ID", "Spanish Score", "English Score", "Social Studies Score", "Science Score"])
            for e in students_list:
                writer.writerow([e["Name"], e["Section"], e["Student ID"], e["Spanish Score"], e["English Score"], e["Social Studies Score"], e["Science Score"]])
        return True
    except Exception:
        return False

def import_to_csv(path):
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students_list.clear()
            for row in reader:
                students_list.append({
                    "Name": row["Name"],
                    "Section": row["Section"],
                    "Student ID": row["Student ID"],
                    "Spanish Score": float(row["Spanish Score"]),
                    "English Score": float(row["English Score"]),
                    "Social Studies Score": float(row["Social Studies Score"]),
                    "Science Score": float(row["Science Score"])
                })
        return True
    except Exception:
        return False