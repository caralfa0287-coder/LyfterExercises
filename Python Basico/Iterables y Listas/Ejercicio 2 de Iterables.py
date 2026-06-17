my_string = "La vida es bella"

new_string = [my_string[i] for i in range(len(my_string) - 1, -1, -1)]
for char in new_string:
    print(char)

#range(len(my_string) - 1, -1, -1) genera una secuencia de índices que va desde el último índice 
# de la cadena (len(my_string) - 1) hasta el primer índice (0), 
# decrementando en 1 en cada iteración. 
# Esto permite acceder a los caracteres de la cadena en orden inverso.
