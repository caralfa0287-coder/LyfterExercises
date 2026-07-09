class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)
    

def request_dimensions():
    while True:
        try:
            width = float(input("Enter the width of the rectangle: "))
            height = float(input("Enter the height of the rectangle: "))
            if width <= 0 or height <= 0:
                print("Width and height must be positive numbers. Please try again.")
                continue
            return width, height
        except ValueError:
            print("Please enter valid numbers for width and height.")

width, height = request_dimensions()
my_rectangle = Rectangle(width, height)

print("Area:", my_rectangle.get_area())
print("Perimeter:", my_rectangle.get_perimeter())