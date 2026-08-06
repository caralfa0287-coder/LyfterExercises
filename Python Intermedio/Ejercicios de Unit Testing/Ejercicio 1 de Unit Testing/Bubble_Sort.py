def my_bubble_sort(list_to_sort):
    n = len(list_to_sort)
        
    for i in range(n): 
            swapped = False
            for j in range(0, n - i - 1):
                current_element = list_to_sort[j]
                next_element = list_to_sort[j+1]
    
                if current_element > next_element:
                    list_to_sort[j] = next_element
                    list_to_sort[j + 1] = current_element
                    swapped = True
    
            if not swapped:
                break
    
    return list_to_sort

def validated_bubble_sort(list_to_sort,): 
        if len(list_to_sort) == 0:
            raise ValueError("Error: La lista no puede estar vacía")

        for element in list_to_sort:
            if not list_to_sort or not isinstance(element, (int, float)):
                raise TypeError("Error: La entrada debe ser una lista numérica")

        return my_bubble_sort(list_to_sort)


