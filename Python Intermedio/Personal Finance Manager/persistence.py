import json
import os
from logic import FinanceManager

Categories_File = "categories.json"
Movements_File = "movements.json"

def save_data(manager: FinanceManager):
    export_categories = [{"name": category.name, "color": category.color} for category in manager.categories]
    with open(Categories_File, "w", encoding="utf-8") as f:
        json.dump(export_categories, f, indent=4)

    movements_dict = [
        {
            "type": movement.type, 
            "title": movement.title, 
            "amount": movement.amount, 
            "category": movement.category,
            "date_str": movement.date_str
        }
            for movement in manager.movements
    ]

    with open(Movements_File, "w", encoding="utf-8") as f:
        json.dump(movements_dict, f, indent=4)


def import_data(manager: FinanceManager):
    if os.path.exists(Categories_File):
        with open(Categories_File, "r", encoding="utf-8") as f:
            categories_data = json.load(f)
            for item in categories_data:
                if isinstance(item, dict):
                    manager.add_category(item["name"], item["color"])
                else:
                    manager.add_category(str(item), "#FFFFFF")


    if os.path.exists(Movements_File):
        with open(Movements_File, "r", encoding="utf-8") as f:
            movements_data = json.load(f)
            manager.movements = []
            for movement in movements_data:
                manager.add_movement(
                    type=movement["type"],
                    title=movement["title"],
                    amount=movement["amount"],
                    category=movement["category"],
                    date_str=movement.get("date_str", "10/08/2026")
                )
