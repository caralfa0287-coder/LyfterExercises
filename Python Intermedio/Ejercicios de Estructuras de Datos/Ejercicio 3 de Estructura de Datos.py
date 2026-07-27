class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def push_left(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            new_node.right = self.root
            self.root = new_node

    def push_right(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            new_node.left = self.root
            self.root = new_node

    def pop_left(self):
        if not self.root:
            print("Error: Empty Structure.")
            return None
        
        value = self.root.value
        
        if not self.root.left and not self.root.right:
            self.root = None
        elif self.root.right:
            self.root = self.root.right
        else:
            self.root = self.root.left
            
        return value

    def pop_right(self):
        if not self.root:
            print("Error: Empty Structure.")
            return None
            
        value = self.root.value
        
        if not self.root.left and not self.root.right:
            self.root = None
        elif self.root.left:
            self.root = self.root.left
        else:
            self.root = self.root.right
            
        return value

    def show(self):
        if not self.root:
            print("Empty Structure")
            return
        
        self._inorder_traversal(self.root)
        print() 

    def _inorder_traversal(self, actual_node):
        if actual_node:
            self._inorder_traversal(actual_node.left)

            print(f"[{actual_node.value}]", end=" ")

            self._inorder_traversal(actual_node.right)

#----Ejemplo de Uso-----

my_tree = BinaryTree()
my_tree.push_right(10)
my_tree.push_right(20)
my_tree.push_left(5)
my_tree.show()