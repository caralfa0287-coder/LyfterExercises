
def print_args_and_return(func):
    def wrapper(*args, **kwargs):
        print(f"  args: {args}")
        print(f"  kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"  Return: {result}\n")
        return result
    return wrapper


@print_args_and_return
def add_and_multiply(a, b, multiplier=1):
    result = (a + b) * multiplier
    return result


# Example usage:
add_and_multiply(2, 4, multiplier=5)
