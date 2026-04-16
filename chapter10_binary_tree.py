class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 


    def show_node(self):
        print(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.connections = []

    # O(log n) = average | O(n) = worst 
    def insert(self, value):
        new = Node(value)
        if self.root is None:
            self.root = new
        else:
            current = self.root
            while True:
                father = current
                #Left
                if value < current.value:
                    current = current.left
                    if current is None:
                        father.left = new
                        self.connections.append(str(father.value) + ' -> ' + str(new.value))
                        return
                #Right
                else:
                    current = current.right
                    if current is None:
                        father.right = new
                        self.connections.append(str(father.value) + ' -> ' + str(new.value))
                        return
                    

tree = BinarySearchTree()
tree.insert(53)
tree.insert(30)
tree.insert(14)
tree.insert(39)
tree.insert(9)
tree.insert(23)
tree.insert(34)
tree.insert(49)
tree.insert(72)
tree.insert(61)
tree.insert(84)
tree.insert(79)
