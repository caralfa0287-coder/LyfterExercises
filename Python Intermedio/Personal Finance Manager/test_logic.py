import unittest
from datetime import datetime, timedelta
from logic import FinanceManager

class TestFinanceManager(unittest.TestCase):

    def setUp(self):
        self.manager = FinanceManager()

    # 1. Prueba: Crear categoría exitosamente
    def test_create_successful_category(self):
        cat ="Food"
        color =  "#FF5733"
        result = self.manager.add_category(cat, color)
        self.assertTrue(result)
        self.assertIn("Food", self.manager.get_categories_list())

    # 2. Prueba: Evitar la creación de categorías duplicadas aun esten escritas en minúsculas
    def test_avoid_duplicate_category(self):
        self.manager.add_category("Transport", "#33FF57")
        result_duplicate = self.manager.add_category("transport", "#33FF57")
        self.assertFalse(result_duplicate)
        self.assertEqual(len(self.manager.categories), 1)

    # 3. Prueba: Agregar movimiento exitoso (Ingreso)
    def test_add_successful_movement(self):
        self.manager.add_category("Salary")
        result = self.manager.add_movement(
            type="Income", title="Bi-weekly payment", amount=1500.0, category="Salary", date_str="10/08/2026"
        )
        self.assertTrue(result)
        self.assertEqual(len(self.manager.movements), 1)

    # 4. Prueba: Bloquear movimiento si la categoría no existe, agregar un gasto sin haber creado la categoría "Health" previamente
    def test_block_movement_without_category(self):
        result = self.manager.add_movement(
            type="Expense", title="Dentist", amount=150.0, category="Health", date_str="10/08/2026"
        )
        self.assertFalse(result)
        self.assertEqual(len(self.manager.movements), 0)

    # 5. Prueba: Bloquear movimientos con monto igual a cero
    def test_block_movement_amount_zero(self):
        self.manager.add_category("Others")
        result = self.manager.add_movement(
            type="Expense", title="Invalid", amount=0.0, category="Others", date_str="10/08/2026"
        )
        self.assertFalse(result)

    # 6. Prueba: Bloquear fechas con formato incorrecto
    def test_validate_incorrect_date_format(self):
        self.manager.add_category("Food")
        result = self.manager.add_movement(
            type="Expense", title="Dinner", amount=30.0, category="Food", date_str="2026/12/25"
        )
        self.assertFalse(result)

    # 7. Prueba: Bloquear estrictamente fechas en el futuro
    def test_block_future_dates(self):
        self.manager.add_category("Entertainment")
        # Calcular el día de mañana dinámicamente para que la prueba nunca quede obsoleta
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        result = self.manager.add_movement(
            type="Expense", title="Future Concert", amount=120.0, category="Entertainment", date_str=tomorrow
        )
        self.assertFalse(result)

    # 8. Prueba: Cálculo exacto del Balance Neto (Ingresos y Gastos Negativos)
    def test_calculate_net_balance(self):
        self.manager.add_category("General")
        # Registrar un ingreso de +2000
        self.manager.add_movement("Income", "Prize", 2000.0, "General", "01/08/2026")
        # Registrar un gasto de -500
        self.manager.add_movement("Expense", "Rent", -500.0, "General", "02/08/2026")
        # Registrar un gasto de 100 (positivo, pero el gestor debe saber restarlo por ser "Expense")
        self.manager.add_movement("Expense", "Market", 100.0, "General", "03/08/2026")
        calculate_balance = self.manager.get_total_balance()
        self.assertEqual(calculate_balance, 1400.0)

    # 9. Prueba: Funcionamiento correcto del filtro por rango de fechas
    def test_filter_movements_by_date(self):
        self.manager.add_category("Filters")
        self.manager.add_movement("Income", "Transf 1", 100.0, "Filters", "05/07/2026")
        self.manager.add_movement("Income", "Transf 2", 200.0, "Filters", "10/07/2026")
        self.manager.add_movement("Income", "Transf 3", 300.0, "Filters", "15/07/2026")
        filters = self.manager.filter_by_date("08/07/2026", "12/07/2026")
        self.assertEqual(len(filters), 1)
        self.assertEqual(filters[0].title, "Transf 2")

if __name__ == "__main__":
    unittest.main()