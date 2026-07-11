import actions
import data


def show_menu():
    print("Please select one of the following options:")
    print("1. Add student")
    print("2. View students")
    print("3. Update student")
    print("4. Delete student")
    print("5. View scores average")
    print("6. View Students Scores Top3")
    print("7. View failed students")
    print("8. Export to CSV file")
    print("9. Import from CSV file")
    print("10. Exit")


def get_user_choice():
    
    while True:
        show_menu()
        try:
            choice = input("Enter your choice: ")
        
            if not choice.isdigit() or int(choice) < 1 or int(choice) > 10:
                print("Please enter a valid option.")
                continue
            match choice:
                case "1": 
                    actions.add_student()
                case "2": 
                    actions.display_students_info()
                case "3": 
                    actions.modify_record()
                case "4": 
                    actions.delete_students()
                case "5": 
                    actions.calculate_average(students_list = data.obtaining_students())
                case "6": 
                    actions.show_top3()
                case "7": 
                    actions.display_failed_students()
                case "8": 
                    data.export_data()
                case "9": 
                    data.import_data()
                case "10":
                    confirmation = input(" Do you want save data before exiting? (y/n): ").lower()
                    if confirmation == "y":
                        data.export_data()
                    print("Exiting...")
                    break
        except ValueError:
            print("Please enter a valid option.")   

