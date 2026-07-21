from datetime import datetime
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args):
        today = datetime.now()
        result = func(*args)
        print(f"Func: '{func.__name__}' - args: {args} - [{today}] - Resultado: {result}")
        print(f"Resultado {result}")
        return result
    return wrapper

def validate_number(func):
    @wraps(func)
    def wrapper(*args):
        if len(args) < 2:
            raise ValueError("Two arguments are required.")
        a, b = args[0], args[1]
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers.")
        return func(*args)
    return wrapper

@validate_number
@log_call
def multiply(*args):
    a, b = args[0], args[1]
    return a * b


# Example usage:
result1 = multiply(3, 4)
result2 = multiply(5, 6)