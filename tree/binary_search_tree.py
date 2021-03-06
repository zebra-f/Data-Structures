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

    def search(self, data):
        if self.data == data:
            return True
        elif data > self.data and self.right:
            return self.right.search(data)
        elif data < self.data and self.left:
            return self.left.search(data)
        else:
            return False

    def min_value(self):
        if self.left:
            return self.left.min_value()
        else:
            return self.data
    
    def max_value(self):
        if self.right:
            return self.right.max_value()
        else:
            return self.data

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_value = self.right.min_value()
            self.data = min_value
            self.right = self.right.delete(min_value)

        return self


    def in_order_traversal(self):
        '''returns an ordered list of all nodes in a binary tree'''
        bst_data = []

        if self.left:
            bst_data += self.left.in_order_traversal()
        
        bst_data.append(self.data)

        if self.right:
            bst_data += self.right.in_order_traversal()

        return bst_data

    def pre_order_traversal(self):
        bst_data = []
        
        stack = [self]  # stack data structure, depth first search
        while len(stack) > 0:
            bst_data.append(stack[-1].data)
            
            temp = stack.pop()
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        
        return bst_data

    def post_order_traversal(self):
        bst_data = []
        
        stack = [self]  # stack data structure, depth first search
        while len(stack) > 0:
            bst_data.append(stack[-1].data)
            
            temp = stack.pop()
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        
        return bst_data[::-1]

    def level_order_traversal(self):
        bst_data = []

        queue = [self]  # queue data structure, breadth first search
        while len(queue) > 0:
            bst_data.append(queue[-1].data)
            
            if queue[-1].left:
                queue.insert(0, queue[-1].left)
            if queue[-1].right:
                queue.insert(0, queue[-1].right)

            queue.pop()
        
        return bst_data

    


h = BinarySearchTree(15)


h.add_child(12)
h.add_child(27)
h.add_child(7)
h.add_child(14)
h.add_child(20)
h.add_child(88)
h.add_child(23)

print(h.in_order_traversal())
print(h.level_order_traversal())
print(h.pre_order_traversal())
print(h.post_order_traversal())

print(h.search(13))
print(h.search(23))

print(h.min_value())
print(h.max_value())

print(h.delete(27))
print(h.level_order_traversal())