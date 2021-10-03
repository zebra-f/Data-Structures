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

    def __len__(self):
        ''' len(1 ---> 2 ---> 4 ---> None) == 3
        '''
        counter = 0
        itr = self.head
        while itr:  
            itr = itr.next_node
            counter += 1

        return counter

    def remove_at_index(self, index):
        if index < 0 or index > self.__len__():
            raise Exception('Not a valid index')
        elif index == 0:
            self.head = self.head.next_node
            return
        
        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1:
                itr.next_node = itr.next_node.next_node
                break
            itr = itr.next_node
            counter += 1

    def insert_at_index(self, index, data):
        if index < 0 or index > self.__len__():
            raise Exception('Not a valid index')
        elif index == 0:
            self.insert_at_beginning(data)
            return
        elif index == self.__len__():
            self.insert_at_end(data)
            return
        
        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1:
                itr.next_node = Node(data, itr.next_node)
                break
            
            itr = itr.next_node
            counter += 1

    def replace_at_index(self, index, data):
        if index < 0 or index > self.__len__() - 1:
            raise Exception('Not a valid index')
        
        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1:
                itr.next_node = Node(data, itr.next_node.next_node)
                break
            
            itr = itr.next_node
            counter += 1

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


# work in progress 
# x = LinkedList()
