# Analice la siguiente función:

def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")

# ¿Cuál es la complejidad temporal?
# R. La complejidad temporal de la función print_all_pairs es O(n^2), donde n es el número de claves en el diccionario my_dict.

# ¿Cuanto dura si hay 1 millón de claves?
# R. Si hay 1 millón de claves, la función realizará 1 millón * 1 millón = 1 billón de iteraciones, lo que resultará en un tiempo de ejecución muy largo y poco práctico.