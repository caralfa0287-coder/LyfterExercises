class Person:
    def __init__(self, name):
        self.name = name
        



class Bus:
    max_passengers = 3
    
    def __init__(self):
        self.passengers = []

    def pick_up_passengers(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"¡{person.name} has boarded the bus!")
        else:
            print("The bus is full. No more passengers can be added.")

    def drop_off_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} has gotten off the bus.")
        else:
            print(f"{person.name} is not on the bus.")



my_bus = Bus()


person1 = Person("Ana")
person2 = Person("Juan")
person3 = Person("Carlos")
person4 = Person("Sofia")

my_bus.pick_up_passengers(person1)
my_bus.pick_up_passengers(person2)
my_bus.pick_up_passengers(person3)      
my_bus.pick_up_passengers(person4) # This should indicate that the bus is full


my_bus.drop_off_passenger(person2)  # Juan gets off the bus
my_bus.pick_up_passengers(person4)  # Sofia can now board the bus
