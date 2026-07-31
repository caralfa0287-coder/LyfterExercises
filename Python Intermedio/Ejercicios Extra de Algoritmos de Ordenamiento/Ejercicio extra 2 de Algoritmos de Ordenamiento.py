def my_bubble_sort(list_to_sort):
    n = len(list_to_sort)
    iteraciones = 0
    intercambios = 0
    
    for index in range(n):
        swapped = False
        iteraciones += 1
        for index in range(0, n - index - 1):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index+1]

            if current_element > next_element:
                list_to_sort[index] = next_element
                list_to_sort[index + 1] = current_element
                swapped = True
                intercambios += 1

        if not swapped:
            break

    return list_to_sort, iteraciones, intercambios

#----Ejemplo de Uso----

my_list = [4, 3, 5, 1, 2]
my_list, iteraciones, intercambios = my_bubble_sort(my_list)

print(f"Lista ordenada: {my_list}")
print(f"Iteraciones: {iteraciones}")
print(f"Intercambios: {intercambios}")