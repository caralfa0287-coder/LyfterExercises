class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        return value
    
    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
            return
        current = self.top
        while current is not None:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

    def bubble_sort(self):
        if self.top is None or self.top.next is None:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.top
            while current.next is not None:
                if current.value > current.next.value:
                    temp = current.value
                    current.value = current.next.value
                    current.next.value = temp
                    
                    swapped = True
                
                current = current.next


#----Ejemplo de Uso----

my_stack = Stack()
my_stack.push(15)
my_stack.push(3)
my_stack.push(42)
my_stack.push(8)
my_stack.print_stack()
my_stack.bubble_sort()
my_stack.print_stack()
