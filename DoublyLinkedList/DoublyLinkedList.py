"""
This file contains constructor and methods for doubly linked list

"""

class Node:
    """
    Class for creating a node of doubly linked list
    
    Node takes one argument for the value. 
    There are two pointers to the node. "prev" will point to previous node and "next" will point to the next node.
    
    """
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    Class for creating the doubly linked list. 
    
    Class constructor takes only one argument for the value of the starting node. 
    
    """
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        """
        Method for appending the doubly linked list. 
        
        The edge case for this method are as follows:
        1. When the list is empty in the beginning i.e. when head and tail both point to "None"
        2. When the list has one or more nodes
        
        """
        # Create a new node with the given value
        new_node = Node(value)

        # Condition where the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        # Conidtion where the list has one or more nodes.
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length+=1
        return True
    
    def pop(self):
        """
        Method to pop the last item of the doubly linked list. The working is similar to what happens in a linked 
        list. 
        
        The edge cases for this are as follows:
        1. There are no elemets in the list
        2. There is only one element in the list
        3. There are two or more elements in the list
        
        """
        # Set a variable pointing towards tail
        temp = self.tail

        # Condition where there are no elements in the list
        if self.head is None:
            return None
        
        # Condition where there is only one item in the list
        if self.length == 1:
            self.head = None
            self.tail = None  

        # Condition where there are two or more elments in the list 
        else:
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
            self.length-=1

        return temp.value
    
    def prepend(self, value):
        """
        This method will add one node at the beginning of the linked list
        
        The edge cases for this methods are as follows:
        1. There are no elements in the list.
        2. There are one or more elements in the list
        
        """
        # Creating new node
        new_node = Node(value)

        # Condition where there are no elements in the list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        # Condition where there are one or more elements in the list
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length+=1
        return True

    def print_list(self):
        """
        Method for priting the contents of the doubly linked list
        
        This method will iterate over the list and print the value of each node. The time complexity is O(n)
        
        """
        temp = self.head
        for _ in range (self.length):
            print(temp.value)
            temp = temp.next
    

if __name__ == "__main__":
    my_doubly_linked_list = DoublyLinkedList(7)
    print("DLL before appending: ")
    my_doubly_linked_list.print_list()

    my_doubly_linked_list.append(3)
    print("DLL after appending: ")
    my_doubly_linked_list.print_list()

    # Test code for pop method
    # Starting with two nodes
    print(my_doubly_linked_list.pop())
    # With only one node
    print(my_doubly_linked_list.pop())    
    # With no nodes
    print(my_doubly_linked_list.pop())

    # Test code for prepend method
    print(my_doubly_linked_list.prepend(3))
    print(my_doubly_linked_list.prepend(7))
