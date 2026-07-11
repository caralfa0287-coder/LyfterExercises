from abc import  ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permissions(self, permission):
        pass    

class AdminUser(User):
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Admin"

    def has_permissions(self, permission):
        return permission in ["read", "write", "delete", "modify"]
    
class RegularUser(User):
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Regular"

    def has_permissions(self, permission):
        return permission in ["read"]
    
user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(user1.has_permissions("delete"))  
print(user2.has_permissions("delete"))   
