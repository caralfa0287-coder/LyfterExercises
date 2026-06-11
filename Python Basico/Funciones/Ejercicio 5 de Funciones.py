#Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.

def count_uppercase_lowercase(text):
    uppercase = 0
    lowercase = 0
    for caracter in text:
        if caracter.isupper():
            uppercase += 1
        elif caracter.islower():
            lowercase += 1
    return (f" Theres {uppercase} upper cases and {lowercase} lower cases ")


def main():
    text = "I love Nación Sushi"
    print(count_uppercase_lowercase(text))


main()