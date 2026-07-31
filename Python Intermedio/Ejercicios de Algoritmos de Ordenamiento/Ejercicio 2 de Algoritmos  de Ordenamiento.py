def my_reverse_bubble_sort(list_to_sort):
    n = len(list_to_sort)
    for i in range(n):
        swapped = False
        for j in range(n - 1, i,  - 1):
            if list_to_sort[j] < list_to_sort[j -1]:
                list_to_sort[j], list_to_sort[j -1] = list_to_sort[j -1], list_to_sort[j]
                swapped = True

        if not swapped:
            break

    return list_to_sort

#----Ejemplo de Uso----

my_list = [64, 34, 25, 12, 22, 11, 10]
print(my_list)
new_list = my_reverse_bubble_sort(my_list)

print(new_list)

