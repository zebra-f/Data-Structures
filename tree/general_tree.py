class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def get_level(self):
        parent = self.parent 
        level = 0
        while parent:
            level += 1
            parent = parent.parent
        
        return level

    def print_tree(self):
        level = self.get_level() * ' ' * 4 
        print(f"-{level + '|___' if self.parent else ' ' * 4}{self.data}")
        
        if self.children:
            for child in self.children:
                child.print_tree()

      
# {self.parent.data if self.parent else 'no parent'}
x10 = TreeNode(10)
x8 = TreeNode(8)
x9 = TreeNode(9)
x7 = TreeNode(7)
x10.add_child(x8)
x10.add_child(x9)
x8.add_child(x7)
x4 = TreeNode(4)
x12 = TreeNode(12)
x8.add_child(x4)
x4.add_child(x12)

x10.print_tree()
print(x10.get_level())