import random

secret_number = random.randint(1, 10)
attempts = 1

print ("Adivina el Número")
print ("Estoy pensando en un número entre el 1 y el 10.")
number = int(input("¿Cuál es el número? "))
while number != secret_number:
    attempts += 1
    if number < secret_number:
        print("Casi pero no, intentalo de nuevo.")
    else:
        print("Casi lo logras, intentalo de nuevo.")
    number = int(input("¿Cuál es el número? "))

print(f"¡Felicidades! Adivinaste el número en {attempts} intentos.")