class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def print_forward(self):
        current = self.head
        res = []
        while current:
            res.append(current.data)
            current = current.next
        print(" -> ".join(res))

    def print_backward(self):
        current = self.tail
        res = []
        while current:
            res.append(current.data)
            current = current.prev
        print(" -> ".join(res))


# ----Ejemplo de Uso----

dll = DoublyLinkedList()
dll.append("A")
dll.append("B")
dll.append("C")
dll.print_forward()
dll.print_backward()

dll.prepend("X")
dll.print_forward()
dll.print_backward()

dll.delete("B")
dll.print_forward()
dll.print_backward()