from functools import wraps

def numbers_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        if not all(isinstance(arg, (int, float)) for arg in all_args):
            raise TypeError("¡Error! All arguments must be integers or floats.")
        return func(*args, **kwargs)
    return wrapper

# --- Example usage ---

@numbers_only
def calculate_area(base, hight):
    return base * hight

# Correct usage
print("Area:", calculate_area(5, 4.5)) 

# Incorrect usage (uncommenting the next line will raise the exception)
# calculate_area(5, "four")