class Node:
    
    def __init__(self, data=None, next_node=None):
        self.data = data  # data
        self.next_node = next_node  # pointer
    

class LinkedList:
    
    def __init__(self):
        self.head = None  # 'potential' head node of the linked list
    
    def insert_at_beginning(self, data):
        head_node = Node(data, self.head)  
        self.head = head_node  # head node of the linked list 

    def insert_at_end(self, data):
        if self.head is None: 
            self.head = Node(data, None)  # tail node of the linked list
            return


# work in progress