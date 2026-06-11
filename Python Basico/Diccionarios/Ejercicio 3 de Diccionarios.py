list_of_keys = ["access_level", "age"]
employee = {"name":"John", "email": "john@ecorp.com",
            "access_level": 5, "age": 28}

for employee_info in [employee.pop(key) for key in list_of_keys]:
    print(f"Deleted item: {employee_info}")
print(employee)