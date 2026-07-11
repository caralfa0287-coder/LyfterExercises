class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"Brand: {self._brand}, Year: {self._year}"  
    
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self._model = model

    def get_info(self):
        return f"{super().get_info()}, Model: {self._model}"
    
class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self._type = type

    def get_info(self):
        return f"{super().get_info()}, Type: {self._type}"
    
vehicle1 = Car("Toyota", 2024, "Tacoma")
vehicle2 = Motorcycle("Honda", 2019, "Sport")

print(vehicle1.get_info())
print(vehicle2.get_info())