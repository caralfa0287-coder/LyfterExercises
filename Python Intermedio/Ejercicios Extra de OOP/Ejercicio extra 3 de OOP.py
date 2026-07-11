class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} has been added to the inventory.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"{product.name} has been removed from the inventory.")
        else:
            print(f"{product.name} is not in the inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for product in self.products:
            print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value


product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)
product3 = Product("Monitor", 15000, 1)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

inventory.display_inventory()
print(f"Total inventory value: {inventory.total_inventory_value()}")