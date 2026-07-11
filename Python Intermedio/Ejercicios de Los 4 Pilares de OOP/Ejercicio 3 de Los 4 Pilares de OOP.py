class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def greet(self):
        print(f"My name is {self.name} and my ID is {self.id}.")

class ManagerMixin:
    def __init__(self, department):
        self.department = department
        print(f"Hello, I am the manager of the {self.department} department.")

class NotificationMixin:
    def send_notification(self, message):
        print(f"Sending notification: {message}")

class Employee(Person, ManagerMixin, NotificationMixin):
    def __init__(self, name, id, department):
        Person.__init__(self, name, id)
        ManagerMixin.__init__(self, department)
        NotificationMixin.__init__(self)

class Developer(Person, NotificationMixin):
    def __init__(self, name, id):
        Person.__init__(self, name, id)
        NotificationMixin.__init__(self)

        
# Example usage:
employee = Employee("Alice", 12345, "Sales")
employee.greet()
employee.send_notification("You have a new task assigned.")

developer = Developer("Charlie", 54321)
developer.greet()
developer.send_notification("Working on the new task.")