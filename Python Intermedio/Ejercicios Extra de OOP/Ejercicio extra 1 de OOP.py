class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

my_rectangle = Rectangle(250, 300)

print("Area:", my_rectangle.get_area())
print("Perimeter:", my_rectangle.get_perimeter())