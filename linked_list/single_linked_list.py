class Node:
    
    def __init__(self, data=None, next_node=None):
        self.data = data  # data
        self.next_node = next_node  # pointer
    

class LinkedList:
    
    def __init__(self):
        self.head = None  # 'potential' head node (instance of the class Node) of the linked list
    
    def insert_at_beginning(self, data):
        head_node = Node(data, self.head)  
        self.head = head_node  # head node of the linked list 

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)  # tail node of the linked list
            return

        itr = self.head
        while itr.next_node:
            itr = itr.next_node

        itr.next_node = Node(data, None)


    def __repr__(self):
        """ Beginning- left side
            End- right side 
        """
        linked_list = ''
        
        itr = self.head
        while itr:
            linked_list += str(itr.data) + ' ---> '
            itr = itr.next_node

        return linked_list + 'None'

x = LinkedList()
x.insert_at_end(19)
x.insert_at_beginning(5)
x.insert_at_beginning(17)
x.insert_at_end(500)
x.insert_at_beginning(33)
x.insert_at_beginning(2)
x.insert_at_end(7)
x.insert_at_beginning(87)

print(x)

# work in progress