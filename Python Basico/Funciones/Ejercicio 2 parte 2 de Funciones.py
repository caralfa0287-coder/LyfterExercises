#Intente acceder a una variable global desde una función y cambiar su valor.
variable = 8

def modify_global_variable():
    variable = variable*2   
    print (variable)


modify_global_variable()

# En python es imposible modificar una variable global desde una funcion, 
# para esto utilizamos el comando 'global' para poder modificar la variable
# Vease archivo 'Ejercicio 2 parte 3 de Funciones.