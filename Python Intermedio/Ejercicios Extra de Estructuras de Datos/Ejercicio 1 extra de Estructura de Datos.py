class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data
    
    def print_all(self):
        current = self.front
        result = ""
        while current is not None:
            result += current.data
            if current.next is not None:
                result += " -> "
            current = current.next
        print(result)

# ---Ejemplo de Uso--- 

q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.print_all()
first_element = q.dequeue()
print(first_element)
q.print_all()