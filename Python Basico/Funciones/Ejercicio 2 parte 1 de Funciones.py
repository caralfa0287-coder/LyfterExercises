#Intente acceder a una variable definida dentro de una función desde afuera.
def inside_function():
    variable_inside_function = "I am inside the function"
    print(variable_inside_function)


inside_function()
print(variable_inside_function)

# El código da error ya que es imposible de acceder a una variable local desde afuera de la función

