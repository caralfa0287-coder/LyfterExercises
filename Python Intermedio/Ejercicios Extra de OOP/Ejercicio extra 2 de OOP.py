class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "It makes a sound"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
dog = Dog("Firulais")
cat = Cat("Michi")   

print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")