# Versión 1:

def manual_add(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

# Versión 2:

def add_formula(n):
    return n * (n + 1) // 2


# ¿Cuál es la complejidad de cada versión?
# R. La complejidad de la versión 1 (manual_add) es O(n), ya que realiza una iteración desde 1 hasta n, sumando cada número al resultado.
# La complejidad de la versión 2 (add_formula) es O(1), ya que utiliza una fórmula matemática para calcular la suma sin necesidad de iterar.

#¿Qué versión usaría si n = 1 000 000 000? ¿Por qué?
# R. Usaría la versión 2 (add_formula) si n = 1 000 000 000, porque su complejidad es O(1), lo que significa que el tiempo de ejecución no depende del tamaño de la entrada. 
# Esto hace que sea mucho más eficiente para valores grandes de n, 
# mientras que la versión 1 (manual_add) sería muy lenta y consumiría muchos recursos debido a su complejidad O(n).