#Cree una función que le dé la vuelta a un string y lo retorne.

def reversed_string (string):
    new_string = ""
    for caracter in string:
        new_string = caracter + new_string
    return new_string


def main():
    string = "Hola Mundo"
    print(reversed_string(string))


main()