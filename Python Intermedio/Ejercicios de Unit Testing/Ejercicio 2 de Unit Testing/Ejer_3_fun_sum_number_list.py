#Cree una función que retorne la suma de todos los números de una lista

def sum_number_list(numbers_list):
    total = 0
    for number in numbers_list:
        total += number
    return total


def main():
    numbers_list = [1, 2, 3, 4, 5]
    print(sum_number_list(numbers_list))


if __name__ == "__main__":
    main()
