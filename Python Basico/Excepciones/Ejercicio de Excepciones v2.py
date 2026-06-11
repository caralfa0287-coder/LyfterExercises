def show_menu():
    print("Operaciones: 1.Suma, 2.Resta, 3.Multiplicación, 4.División, 5.Borrar resultado, salir")


def input_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print(f"Error [ValueError]: Entrada inválida. Ingrese un número.")

def input_second_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print(f"Error [ValueError]: Entrada inválida. Ingrese un número.")

def operations(num1, num2, operation):
    if operation == '1': return num1 + num2
    if operation == '2': return num1 - num2
    if operation == '3': return num1 * num2
    if operation == '4':
        try:
            num1 / num2
        except ZeroDivisionError:
            if num2 == 0:
                print("Error [ZeroDivisionError]: División por cero.")
    return num1

def calculator():
    print("Calculadora")
    print("Para salir, escribe 'salir' en la operación.")
    actual = input_number("Ingrese un número inicial: ")

    while True:
        print(f"\n>> Número actual: {actual}")
        show_menu()
        operation = input("Seleccionar una opción (1-5): ").lower()
    
        if operation == 'salir':
            print(f"Resultado final: {actual}, Cerrando calculadora. ¡Adiós!")
            break

        if operation == "5":
            actual = 0.0
            continue

        if operation in ['1', '2', '3', '4', "5"]:
            second_number = input_second_number("Ingresa otro número: ")
            actual = operations(actual, second_number, operation)
        else:
                print("Error [ValueError]: Entrada inválida. Seleccionar una opción (1-5)")



if __name__ == "__main__":
    calculator()