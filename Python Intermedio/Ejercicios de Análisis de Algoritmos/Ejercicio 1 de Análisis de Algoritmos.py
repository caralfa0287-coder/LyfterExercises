def my_bubble_sort(list_to_sort):
    n = len(list_to_sort) # O(1)
    for index in range(n): # O(n)
        swapped = False # O(1)
        for index in range(0, n - index - 1): # O(log n)
            current_element = list_to_sort[index] # O(1)
            next_element = list_to_sort[index+1] # O(1)

            if current_element > next_element: # O(1)
                list_to_sort[index] = next_element # O(1)
                list_to_sort[index + 1] = current_element # O(1)
                swapped = True # O(1)

        if not swapped: # O(1)
            return # O(1)

# Time complexity: O(log n)