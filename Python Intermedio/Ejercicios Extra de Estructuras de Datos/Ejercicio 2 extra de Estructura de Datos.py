class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next

    def print_all(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))


# ----Ejemplo de Uso----

ll = LinkedList()
ll.insert_front(10)
ll.insert_front(20)
ll.print_all()
ll.insert_back(30)
ll.print_all()
ll.delete(10)
ll.print_all()
