from datetime import datetime
import csv


class Category:
    def __init__(self, name: str, color: str = "#FFFFFF"):
        self.name = name.strip().capitalize()
        self.color = color if color else "#FFFFFF"


class Movement:
    def __init__(self, type: str, title: str, amount: float, category: str, date_str: str):
        self.type = type
        self.title = title.strip()
        amount_clean = str(amount).replace("$", "").replace(",", "").strip()
        self.amount = float(amount_clean)
        self.category = category
        self.date_str = date_str.strip()


class FinanceManager:
    def __init__(self):
        self.movements = []
        self.categories = []


    def add_category(self, name: str, color: str = "#FFFFFF") -> bool:
        clean_name = name.strip().capitalize()
        if not clean_name:
            return False
        if any(category.name == clean_name for category in self.categories):
            return False
        self.categories.append(Category(clean_name, color))
        return True


    def add_movement(self, type: str, title: str, amount: float, category: str, date_str: str) -> bool:
        if not self.categories or not title or not str(title).strip():
            return False
        clean_category = str(category).strip().capitalize()
        if not any(c.name == clean_category for c in self.categories):
            return False  
            
        try:
            amount_num = float(str(amount).replace("$", "").strip())
            if amount_num == 0: return False
        except (ValueError, TypeError):
            return False
        date_clean = str(date_str).strip()
        try:
            obj_date = datetime.strptime(date_clean, "%d/%m/%Y")
        except ValueError:
            try:
                obj_date = datetime.strptime(date_clean, "%Y-%m-%d")
                date_clean = obj_date.strftime("%d/%m/%Y")
            except ValueError:
                return False
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if obj_date > today:
            return False
        correct_type = "Expense" if type.lower() in ["gasto", "expense"] else "Income"
        self.movements.append(Movement(correct_type, title, amount_num, clean_category, date_clean))
        return True


    def get_movements_table(self, movements_to_show=None):
        list_to_use = movements_to_show if movements_to_show is not None else self.movements
        return [
            [
                movement.date_str, 
                movement.type, 
                movement.title, 
                f"${movement.amount:.2f}", 
                movement.category
            ]
            for movement in list_to_use
        ]


    def get_colors_rows(self, movements_to_show=None) -> list:
        list_to_use = movements_to_show if movements_to_show is not None else self.movements
        map_colors = {category.name: category.color for category in self.categories}
        color_configuration = []
        for index, movement in enumerate(list_to_use):
            background_color = map_colors.get(movement.category, "#FFFFFF")
            color_text = "#000000"
            color_configuration.append((index, color_text, background_color))
        return color_configuration


    def get_categories_list(self):
        return [category.name for category in self.categories]


    def filter_by_date(self, start_date: str, end_date: str):
        try:
            start = datetime.strptime(start_date.strip(), "%d/%m/%Y")
            end = datetime.strptime(end_date.strip(), "%d/%m/%Y")
        except ValueError:
            raise ValueError("Invalid date format. Please use DD/MM/YYYY.")
        filtered_movements = []
        for movement in self.movements:
            date_movement = datetime.strptime(movement.date_str, "%d/%m/%Y")
            if start <= date_movement <= end:
                filtered_movements.append(movement)
        return filtered_movements


    def get_total_balance(self, movements_to_calculate=None) -> float:
        list = movements_to_calculate if movements_to_calculate is not None else self.movements
        total = 0.0
        for m in list:
            if m.type == "Expense" and m.amount > 0:
                total -= m.amount
            else:
                total += m.amount
        return total


    def export_to_csv(self, file_name: str = "finance report.csv") -> str:
        if not self.movements:
            raise ValueError("No recorded movements for export.")
        headings = ["Date", "Title", "Amount", "Category", "Type"]
        total_income = 0.0
        total_expenses = 0.0
        with open(file_name, mode="w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f, delimiter=";") 
            writer.writerow(headings)
            for mov in self.movements:
                writer.writerow([mov.date_str, mov.title, f"{mov.amount:.2f}", mov.category, mov.type])
                if mov.type == "Expense":
                    total_expenses += abs(mov.amount)
                else:
                    total_income += mov.amount
            balance_net = total_income - total_expenses
            writer.writerow([]) 
            writer.writerow(["--- FINANCE RESUME ---"])
            writer.writerow(["Total Income:", f"${total_income:.2f}"])
            writer.writerow(["Total Expenses:", f"${total_expenses:.2f}"])
            writer.writerow(["Net Balance:", f"${balance_net:.2f}"])
        return file_name