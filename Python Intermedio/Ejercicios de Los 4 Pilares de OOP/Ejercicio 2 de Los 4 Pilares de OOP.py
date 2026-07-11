from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return 4 * self.side

# Example usage:
circle = Circle(radius=5)   
rectangle = Rectangle(width=250, height=300)
square = Square(side=4)

print(f"Circle area: {circle.calculate_area()}, perimeter: {circle.calculate_perimeter()}")
print(f"Rectangle area: {rectangle.calculate_area()}, perimeter: {rectangle.calculate_perimeter()}")
print(f"Square area: {square.calculate_area()}, perimeter: {square.calculate_perimeter()}")