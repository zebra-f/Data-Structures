class BinarySearchTree:

    # Node
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
        bst_data = []

        if self.left:
            bst_data += self.left.in_order_traversal()
        
        bst_data.append(self.data)

        if self.right:
            bst_data += self.right.in_order_traversal()

        return bst_data

    def level_traversal(self):
        bst_data = []

        queue = [self]  # queue data structure
        while len(queue) > 0:
            bst_data.append(queue[-1].data)
            
            if queue[-1].left:
                queue.insert(0, queue[-1].left)
            if queue[-1].right:
                queue.insert(0, queue[-1].right)

            queue.pop()
        
        return bst_data


h = BinarySearchTree(14)

h.add_child(2)
h.add_child(17)
h.add_child(21)
h.add_child(5)
h.add_child(56)

print(h.in_order_traversal())
print(h.level_traversal())
