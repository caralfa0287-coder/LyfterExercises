name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))
if (age <= 2) :
	print(name + " " + lastname + ":" + " Eres un bebé.")
elif (age <= 10) :
    print(name + " " + lastname + ":" + " Eres un niño.")
elif (age <= 13):
    print(name + " " + lastname + ":" + " Eres un preadolescente.")
elif (age <= 18):
    print(name + " " + lastname +  ":" + " Eres un adolescente.")
elif (age <= 35):
    print(name + " " + lastname + ":" + " Eres un adulto joven.")
elif (age < 65):
    print(name + " " + lastname +  ":" + " Eres un adulto.")
else:
    print(name + " " + lastname + " Eres un adulto mayor.")

