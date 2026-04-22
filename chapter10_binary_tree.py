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
                    

    # O(log n) = average | O(n) = worst 
    def search(self, value):
        current = self.root
        while current.value != value:
            if value < current.value:
                current = current.left
            else:
                current = current.right
            if current is None:
                return None
        return current          


    #root, left, right
    def pre_ordination(self, node:Node):
        if node is not None:
            print(node.value)
            self.pre_ordination(node.left)
            self.pre_ordination(node.right)


    #left, root, right
    def in_order(self, node:Node):
        if node is not None:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)


    #left, right, root
    def post_ordination(self, node:Node):
        if node is not None:
            self.post_ordination(node.left)
            self.post_ordination(node.right)
            print(node.value)


    def delete(self, value):
        if self.root is None:
            print('Empty tree!')
            return
        #find node
        current = self.root
        father = self.root
        is_left = True
        while current.value != value:
            father = current
            #left 
            if value < current.value:
                is_left = True
                current = current.left
            else: #right
                is_left = False
                current = current.right
            if current is None:
                return False
        #node to be deleted it's a leaf
        if current.left is None and current.right is None:
            if current == self.root:
                self.root = None
            elif is_left == True:
                self.connections.remove(str(father.value) + ' -> ' + str(current.value))
                father.left = None
            else:
                self.connections.remove(str(father.value) + ' -> ' + str(current.value))
                father.right = None
        #node to be deleted doesn't have nodes at right
        elif current.right is None:
            self.connections.remove(str(father.value) + ' -> ' + str(current.value))
            self.connections.remove(str(father.value) + ' -> ' + str(current.left.value))
            if current == self.root:
                self.root = current.left
                self.connections.append(str(father.value) + ' -> ' + str(current.left.value))
            elif is_left:
                father.left = current.left
                self.connections.append(str(father.value) + ' -> ' + str(current.left.value))
            else:
                father.right = current.left
                self.connections.append(str(father.value) + ' -> ' + str(current.left.value))
        #node to be deleted doesn't have nodes at left
        elif current.left is None:
            self.connections.remove(str(father.value) + ' -> ' + str(current.value))
            self.connections.remove(str(father.value) + ' -> ' + str(current.right.value))
            if current == self.root:
                self.root = current.right
                self.connections.append(str(father.value) + ' -> ' + str(current.right.value))
            elif is_left:
                father.left = current.right
                self.connections.append(str(father.value) + ' -> ' + str(current.right.value))
            else:
                father.right = current.right
                self.connections.append(str(father.value) + ' -> ' + str(current.right.value))
        else: #node has 2 children
            successor = self.get_successor(current)
            self.connections.remove(str(father.value) + ' -> ' + str(current.value))
            self.connections.remove(str(current.right.value) + ' -> ' + str(successor.value)) #to-do: Bug on this line while trying to delete 39
            self.connections.remove(str(current.value) + ' -> ' + str(current.left.value))
            self.connections.remove(str(current.value) + ' -> ' + str(current.right.value))
            if current == current.root:
                self.connections.append(str(self.root.value) + ' -> ' + str(successor.value))
                self.root = successor
            elif is_left:
                self.connections.append(str(father.value) + ' -> ' + str(successor.value))
                father.left = successor
            else:
                self.connections.append(str(father.value) + ' -> ' + str(successor.value))
                father.right = successor
            self.connections.append(str(successor.value) + ' -> ' + str(current.left.value))
            self.connections.append(str(successor.value) + ' -> ' + str(current.right.value))
            successor.left = current.left
        return True


    def get_successor(self, node:Node):
        father_successor = node
        successor = node
        current = node.right
        while current != None:
            father_successor = successor
            successor = current
            current = current.left
        if successor != node.right:
            father_successor.left = successor.right
            successor.right = node.right
        return successor



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
test_search_72 = tree.search(72)
test_search_49 = tree.search(49)
test_search_51 = tree.search(51)
print()
print('Pre-ordination:')
tree.pre_ordination(tree.root)
print()
print('In order')
tree.in_order(tree.root)
print('Post-ordination:')
tree.post_ordination(tree.root)
print()
print('before 9 deletion')
print(tree.connections)
tree.delete(9)
print()
print('after 9 deletion')
print(tree.connections)
tree.delete(79)
print('after 79 deletion')
print(tree.connections)
tree.delete(100)
print('after trying to delete 100')
print(tree.connections)
print(f'53 successor: {tree.get_successor(tree.root).value}')
print('before delete 39')
tree.delete(39) #ug line 137
print('after trying to delete 39')
print(tree.connections)
