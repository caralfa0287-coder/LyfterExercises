import functools

def repeat_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)  
        return func(*args, **kwargs)  
    return wrapper

@repeat_twice
def greet(name):
    print(f"Hola, {name}")

# Example usage:

greet("Jeanca")
