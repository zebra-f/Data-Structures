class BinarySearchTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        elif data < self.data:
            # left subtree
            if self.left:
                self.left.add_child(data)       
            else:
                self.left = BinarySearchTree(data)
        else:
            # right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        '''returns an ordered list of all nodes in a binary tree'''
        nodes = []

        if self.left:
            nodes += self.left.in_order_traversal()
        
        nodes.append(self.data)

        if self.right:
            nodes += self.right.in_order_traversal()

        return nodes


h = BinarySearchTree(14)

h.add_child(2)
h.add_child(17)
h.add_child(21)
h.add_child(5)
h.add_child(56)

print(h.in_order_traversal())
