import FreeSimpleGUI as sg
from logic import FinanceManager
import persistence
from datetime import datetime


sg.theme("DarkBlue3")


def window_new_category() -> tuple [str, str] | tuple[None, None]:
    layout = [
        [sg.Text("Enter the name of the new category:")],
        [sg.Input(key="-NAME-", size=(25, 1))],
        [sg.Text("Category color")],
        [
            sg.Input(key="-COLOR-", size=(12, 1), default_text="#FFFFFF", readonly=True),
            sg.ColorChooserButton("🎨 Choose Color", target="-COLOR-")
        ],
        [sg.Button("Add"), sg.Button("Cancel")]
    ]
    window = sg.Window("New Category", layout, modal=True)
    name, color = None, None
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            break
        if event == "Add":
            name = values["-NAME-"].strip()
            color = values["-COLOR-"].strip()
            if not name:
                sg.popup_error("Category name cannot be empty.")
            else:
                break
    window.close()
    return name, color


def window_new_movement(type: str, categories: list) -> dict | None:
    today = datetime.now().strftime("%d/%m/%Y")
    layout = [
        [sg.Text(f"Add {type}", font=("Arial", 14, "bold"))],
        [sg.Text("Date (dd/mm/yyyy):"), sg.Input(today, key="-DATE-", size=(15,1))],
        [sg.Text("Title:"), sg.Input(key="-TITLE-")],
        [sg.Text("Amount:"), sg.Input(key="-AMOUNT-", tooltip="Example: -100.50 for expenses, 100.50 for income")],
        [sg.Text("Category:"), sg.Combo(categories, default_value=categories[0] if categories else "", key="-CATEGORY-", readonly=True)],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]
    window = sg.Window(f"New {type}", layout, modal=True)
    data = None
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            break
        if event == "Save":
            date_str = values["-DATE-"].strip()
            title = values["-TITLE-"].strip()
            amount = values["-AMOUNT-"]
            category = values["-CATEGORY-"]
            try:
                obj_date = datetime.strptime(date_str, "%d/%m/%Y")
                obj_today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                if obj_date > obj_today:
                    sg.popup_error("Error: The date cannot be in the future")
                    continue
            except ValueError:
                sg.popup_error("Error: The date must have the format dd/mm/yyyy (e.g., 25/12/2026).")
                continue
            try:
                amount = float(amount.replace("$", ""))
                if amount == 0: raise ValueError("The amount must be a non-zero number.")
                if type == "Income" and amount < 0:
                    sg.popup_error("Error: For income, the amount must be a positive number.")
                    continue
            except ValueError:
                sg.popup_error("The amount must be a valid number (e.g., -50.00 or 100.50).")
                continue
            if not title:
                sg.popup_error("The title cannot be empty.")
                continue
            if not category:
                sg.popup_error("Select a category.")
                continue
            data = {"type": type, "title": title, "amount": amount, "category": category, "date_str": date_str}
            break
    window.close()
    return data


def main_window():
    manager = FinanceManager()
    persistence.import_data(manager)
    headings = ["Date","Type", "Title", "Amount", "Category"]
    def update_window(win, list_movements=None):
        new_data = manager.get_movements_table(list_movements)
        rows_colors = manager.get_colors_rows(list_movements)
        win["-TABLE-"].update(values=new_data, row_colors=rows_colors)
        balance = manager.get_total_balance(list_movements)
        color_text = "#2ECC71" if balance >= 0 else "#E74C3C"
        win["-BALANCE-"].update(value=f"${balance:.2f}", text_color=color_text)
    main_layout = [
        [sg.Text("Personal Finance Manager", font=("Arial", 16,"bold"))],
        [
            sg.Text("Balance Total: ", font=("Arial", 14, "bold")),
            sg.Text("$0.00", font=("Arial", 14, "bold"), key="-BALANCE-")
        ],
        [sg.HSeparator()],
        [
            sg.Text("Start (dd/mm/yyyy):"), sg.Input(key="-DATE_STA-", size=(12, 1)),
            sg.Text("End (dd/mm/yyyy):"), sg.Input(key="-DATE_END-", size=(12, 1)),
            sg.Button("🔍 Filter", key="-FILTER-"),
            sg.Button("🔄 Reset", key="-RESET-")
        ],
        [sg.Table(values=manager.get_movements_table(), headings=headings, max_col_width=25,
                auto_size_columns=True, display_row_numbers=False,
                justification="left", num_rows=10, key="-TABLE-", expand_x=True)],
        [
            sg.Button("➕ Category", key="-ADD_CATEGORY-"),
            sg.Button("📉 Add Expense", key="-ADD_EXPENSE-"),
            sg.Button("📈 Add Income", key="-ADD_INCOME-"),
            sg.Button("📥 Export to CSV", key="-EXPORT-", button_color=("#FFFFFF", "#27AE60"))
        ],
        [sg.Button("Exit", size=(10, 1))]
    ]
    window = sg.Window("Personal Finance Manager", main_layout, finalize=True)
    update_window(window)  
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        if event == "-EXPORT-":
            try:
                name = manager.export_to_csv("finance report.csv")
                sg.popup(f"¡Successfully Export!\n\nThe File '{name}' has been created successfully.", 
                        title="Report Created")
            except ValueError as e:
                sg.popup_error(f"Error to export: {e}")
            except Exception as e:
                sg.popup_error(f"Unexpected error while saving the file: {e}")
        if event == "-FILTER-":
            d_start = values["-DATE_STA-"].strip()
            d_end = values["-DATE_END-"].strip()
            if not d_start or not d_end:
                sg.popup_error("Error: Both date fields (Start and End) must be completed.")
                continue
            try:
                movs_filtered = manager.filter_by_date(d_start, d_end)
                update_window(window, movs_filtered)
            except ValueError as e:
                sg.popup_error(str(e))
        elif event == "-RESET-":
            window["-DATE_STA-"].update("")
            window["-DATE_END-"].update("")
            update_window(window)
        elif event == "-ADD_CATEGORY-":
            category_name, category_color = window_new_category()
            if category_name and category_color:
                if manager.add_category(category_name, category_color):
                    persistence.save_data(manager)
                    update_window(window)
                    sg.popup("Category added successfully with color!")
                else:
                    sg.popup_error("Category already exists or is not valid.")
        elif event in ("-ADD_EXPENSE-", "-ADD_INCOME-"):
            if not manager.get_categories_list():
                sg.popup_error("Error: You cannot record transactions without first creating at least one category..")
                continue
            movement_type = "Expense" if event == "-ADD_EXPENSE-" else "Income"
            if movement_data := window_new_movement(movement_type, manager.get_categories_list()):
                success = manager.add_movement(
                    movement_data["type"],
                    movement_data["title"],
                    movement_data["amount"],
                    movement_data["category"],
                    movement_data["date_str"]
                )
                if success:
                    persistence.save_data(manager)
                    update_window(window)
                    sg.popup("Movement added successfully!")
                else:
                    sg.popup_error("Error: Failed to add movement. Please check the input values.")
    window.close()


if __name__ == "__main__":
    main_window()