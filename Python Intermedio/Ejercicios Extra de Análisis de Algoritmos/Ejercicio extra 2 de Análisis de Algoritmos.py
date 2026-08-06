# Considere los siguientes dos algoritmos:

def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False

def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


# ¿Cuál es la complejidad de cada algoritmo?
# R. La complejidad del algoritmo linear_search es O(n), ya que en el peor de los casos, 
# debe recorrer toda la lista para encontrar el elemento target o determinar que no está presente.
# La complejidad del algoritmo binary_search es O(log n), ya que divide la lista en mitades en cada iteración, 
# reduciendo significativamente el número de elementos a considerar.

# ¿En qué condiciones conviene usar cada uno?
# R. Conviene usar linear_search cuando la lista no está ordenada o es muy pequeña.
# Mientras que binary_search es más eficiente para listas grandes y ordenadas, ya que su complejidad logarítmica permite encontrar elementos mucho más rápido.

# ¿Qué pasa si la lista no está ordenada?
# R. Si la lista no está ordenada, binary_search no funcionará correctamente, ya que depende de la propiedad de orden para dividir la lista y descartar mitades.