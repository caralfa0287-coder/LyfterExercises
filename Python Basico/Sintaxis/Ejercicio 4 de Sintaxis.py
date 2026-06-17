print("Ingresa 3 numeros diferentes y te diré cuál es el mayor.")
number1 = int(input("Número 1: "))
number2 = int(input("Número 2: "))
number3 = int(input("Número 3: "))
if (number1 > number2) and (number1 > number3):
    print("El número mayor es: " + str(number1))
elif (number2 > number1) and (number2 > number3):
    print("El número mayor es: " + str(number2))
else:
    print("El número mayor es: " + str(number3))
    