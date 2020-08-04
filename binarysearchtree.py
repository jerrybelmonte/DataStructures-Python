# BinarySearchTree implementation
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if self.root:
            current = self.root
            while current:
                if new_val > current.value:
                    current = current.right
                else:
                    current = current.left
        else:
            self.root = Node(new_val)

    def search(self, find_val):
        current = self.root
        while current:
            if find_val > current.value:
                current = current.right
            elif find_val < current.value:
                current = current.left
            else:
                break
        if current and current.value == find_val:
            return True
        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Output should be True
print(tree.search(4))
# Output should be False
print(tree.search(6))
