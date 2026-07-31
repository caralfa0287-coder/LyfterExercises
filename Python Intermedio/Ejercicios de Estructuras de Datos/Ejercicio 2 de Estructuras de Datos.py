class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            return None
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return value

    def pop_right(self):
        if self.head is None:
            return None
        value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return value

    def print_deque(self):
        if self.head is None:
            print("Empty deque")
            return
        
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" <-> ".join(elements))

# --- Ejemplo de uso ---
dq = Deque()
dq.push_right(10)
dq.push_right(20)
dq.push_left(5)
dq.print_deque()  

dq.pop_left()
dq.pop_right()
dq.print_deque()  