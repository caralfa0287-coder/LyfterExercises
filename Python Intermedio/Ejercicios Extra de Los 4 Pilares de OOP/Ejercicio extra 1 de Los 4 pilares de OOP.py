class Employee:     
    
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("The salary cannot be negative.")
        self.__salary = value

    def promote(self, percentage: float):
        self.salary += self.salary * percentage

employee1 = Employee("Ana", 1000)
employee1.promote(0.10)

print(employee1.salary)
