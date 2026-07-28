class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        
        if value > self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def print_structure(self, level=0):
        
        if self.right is not None:
            self.right.print_structure(level + 1)
            
        indentation = "    " * level
        print(f"{indentation}── {self.value}")
        
        if self.left is not None:
            self.left.print_structure(level + 1)


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def print_tree(self):
        if self.root is None:
            print("The tree is empty.")
        else:
            self.root.print_structure(0)


# ----Ejemplo de Uso----

my_tree = BinaryTree()
my_tree.insert(20)
my_tree.insert(30)
my_tree.insert(70)
my_tree.insert(20)
my_tree.insert(40)
my_tree.insert(60)
my_tree.insert(80)

my_tree.print_tree()