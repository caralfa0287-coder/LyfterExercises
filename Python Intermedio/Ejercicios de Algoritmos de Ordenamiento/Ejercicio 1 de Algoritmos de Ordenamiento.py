def my_bubble_sort(list_to_sort):
    n = len(list_to_sort)
    for index in range(n):
        swapped = False
        for index in range(0, n - index - 1):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index+1]

            if current_element > next_element:
                list_to_sort[index] = next_element
                list_to_sort[index + 1] = current_element
                swapped = True

        if not swapped:
            return


#----Ejemplo de Uso----

my_list = [64, 34, 25, 12, 22, 11, 90]
my_bubble_sort(my_list)

print(my_list)