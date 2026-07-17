from datetime import date

def validate_age(func):
    def wrapper(user):
        if user.age < 18:
            raise ValueError(f"User {user.name} is under 18 years old.")
        return func(user)
    return wrapper


class User:
    def __init__(self, date_of_birth, name):
        self.date_of_birth = date_of_birth # format: YYYY-MM-DD
        self.name = name

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

# Example usage
@validate_age
def access_restricted_area(user):
    return f"Access granted to {user.name}."    

user1 = User(date(2005, 5, 15), "Albert")
print(access_restricted_area(user1))

user2 = User(date(2010, 8, 20), "Charlie")
print(access_restricted_area(user2))