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
        current_print_level = self.get_level() * ' ' * 4 
        print(f"-{current_print_level + '|___' if self.parent else ' ' * 4}{self.data}")
        
        if self.children:
            for child in self.children:
                child.print_tree()
    
    def print_tree_level(self, level, show_parents=False):
        
        if self.get_level() == level:
            if show_parents:
                print(f"{self.parent.data if self.parent else 'None'}\
                     \n|___{self.data}")
            else:
                print(f"{self.data}")
        
        if self.children:
            for child in self.children:
                child.print_tree_level(level, show_parents)
