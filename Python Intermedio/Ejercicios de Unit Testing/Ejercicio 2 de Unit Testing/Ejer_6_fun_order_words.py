#Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual,
#pero ordenado alfabéticamente.

def order_words(word):
    words = word.split('-')
    words.sort()
    result = '-'.join(words)
    return result


def main():
    word = 'python-variable-funcion-computadora-monitor'
    print(order_words(word))

main()

