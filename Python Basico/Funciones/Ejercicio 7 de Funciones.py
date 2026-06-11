# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def filter_prime(numbers_list):
    return [n for n in numbers_list if is_prime_number(n)]


def main():
    numbers_list = [1, 4, 6, 7, 13, 9, 67 ]
    print(filter_prime(numbers_list))


if __name__ == "__main__":
    main()
