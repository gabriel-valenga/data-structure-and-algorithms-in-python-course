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

    # O(log n) = average | O(n) = worst 
    def insert(self, value):
        new = Node(value)
        if self.root is None:
            self.root = new
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new
                        return
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new
                        return
                    current = current.right

    # O(log n) = average | O(n) = worst 
    def search(self, value):
        current = self.root
        while current:
            if current.value == value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None          

    # root, left, right
    def pre_ordination(self, node):
        if node:
            print(node.value)
            self.pre_ordination(node.left)
            self.pre_ordination(node.right)

    # left, root, right
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)

    # left, right, root
    def post_ordination(self, node):
        if node:
            self.post_ordination(node.left)
            self.post_ordination(node.right)
            print(node.value)

    def get_connections(self):
        result = []

        def dfs(node):
            if node:
                if node.left:
                    result.append(f"{node.value} -> {node.left.value}")
                    dfs(node.left)
                if node.right:
                    result.append(f"{node.value} -> {node.right.value}")
                    dfs(node.right)

        dfs(self.root)
        return result

    def delete(self, value):
        if self.root is None:
            print('Empty tree!')
            return False

        current = self.root
        father = None
        is_left = True

        # find node
        while current and current.value != value:
            father = current
            if value < current.value:
                is_left = True
                current = current.left
            else:
                is_left = False
                current = current.right

        if current is None:
            return False

        # leaf
        if current.left is None and current.right is None:
            if current == self.root:
                self.root = None
            elif is_left:
                father.left = None
            else:
                father.right = None

        # only left child
        elif current.right is None:
            if current == self.root:
                self.root = current.left
            elif is_left:
                father.left = current.left
            else:
                father.right = current.left

        # only right child
        elif current.left is None:
            if current == self.root:
                self.root = current.right
            elif is_left:
                father.left = current.right
            else:
                father.right = current.right

        # two children
        else:
            successor = self.get_successor(current)

            if current == self.root:
                self.root = successor
            elif is_left:
                father.left = successor
            else:
                father.right = successor

            successor.left = current.left

        return True

    def get_successor(self, node):
        father_successor = node
        successor = node
        current = node.right

        while current:
            father_successor = successor
            successor = current
            current = current.left

        if successor != node.right:
            father_successor.left = successor.right
            successor.right = node.right

        return successor


# ================= TESTE =================

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
print(tree.get_connections())

tree.delete(9)

print()
print('after 9 deletion')
print(tree.get_connections())

tree.delete(79)
print('after 79 deletion')
print(tree.get_connections())

tree.delete(100)
print('after trying to delete 100')
print(tree.get_connections())

print(f'53 successor: {tree.get_successor(tree.root).value}')

print('before delete 39')
print(tree.get_connections())

tree.delete(39)

print('after trying to delete 39')
print(tree.get_connections())

print('before delete 30')
print(tree.get_connections())

tree.delete(30)

print('after trying to delete 30')
print(tree.get_connections())

print()
print('Final In-order (should be sorted):')
tree.in_order(tree.root)
