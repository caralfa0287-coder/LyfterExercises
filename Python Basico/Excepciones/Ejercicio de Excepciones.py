def calculator():
    print("Calculadora")
    print("Para salir, escribe 'salir' en la operación.")
    
    try:
        actual = float(input("Ingresa el primer número: "))
    except ValueError:
        print(f"Error [ValueError]: Entrada inválida. Iniciando con 0.")
        actual = 0.0

    while True:
        print(f"\nNúmero actual: {actual}")
        print("Menú de operaciones: 1.Suma, 2.Resta, 3.Multiplicación, 4.División, 5.Borrar resultado, salir")
        
        operation = str(input("Seleccionar una opción (1-5): ").lower())

        if operation == 'salir':
                print(f"Resultado final: {actual}, Cerrando calculadora. ¡Adiós!")
                break
        elif operation == '5':
                actual = float(input("Ingresar nuevo número base: "))
                continue
        elif operation not in ['1', '2', '3', '4']:
                print("Error [ValueError]: Entrada inválida. Seleccionar una opción (1-5)")
                continue

        try:
            second_number = float(input("Ingresa otro número: "))
            if operation == '1':
                actual += second_number
            elif operation == '2':
                actual -= second_number
            elif operation == '3':
                actual *= second_number
            elif operation == '4':
                
                try:
                    second_number != 0
                    actual /= second_number
                except ZeroDivisionError:
                    print("Error [ZeroDivisionError]: División por cero.")
        except ValueError:
            print("Error [ValueError]: Entrada inválida. Por favor ingresa un número.")

if __name__ == "__main__":
    calculator()