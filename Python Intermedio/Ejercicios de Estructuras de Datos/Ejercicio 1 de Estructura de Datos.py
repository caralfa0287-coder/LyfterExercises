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
            print(current.value)
            current = current.next

# Example usage:
my_stack = Stack()
my_stack.push("!")
my_stack.push("World")
my_stack.push("Hello")
my_stack.print_stack()
print(my_stack.pop())  
print(my_stack.pop())  
print(my_stack.pop())  