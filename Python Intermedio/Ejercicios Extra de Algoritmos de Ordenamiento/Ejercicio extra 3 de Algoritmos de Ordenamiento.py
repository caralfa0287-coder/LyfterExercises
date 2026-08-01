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
    try: 
        if len(list_to_sort) == 0:
            raise ValueError("Error: La lista no puede estar vacía")

        for element in list_to_sort:
            if not isinstance(element, (int, float)):
                raise TypeError("Error: La lista contiene elementos no numéricos")

        return my_bubble_sort(list_to_sort)

    except (ValueError, TypeError) as e:
        return str(e)



#----Ejemplo de Uso----

my_list = [5,4,3,2,1]

print(validated_bubble_sort(my_list))