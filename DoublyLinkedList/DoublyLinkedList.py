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
        self.length += 1
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
            self.length -= 1

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

        self.length += 1
        return True
    
    def pop_first(self):
        """
        This method will pop the first element from the doubly linked list and return it.
        
        The edge cases for this method are as follows: 
        1. When the DLL has no elements
        2. When the DLL has two or more elements
        3. When the DLL has only one element
        
        """
        # Case where the DLL has no elements
        if self.head == None:
            return None
        
        temp = self.head # Condition valid when the DLL has one or more elements
        
        # Case where the DLL has only one element
        if self.length == 1:
            self.head = None
            self.tail = None

        # Condition where the DLL has two or more elements
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        
        self.length -= 1
        return temp
    
    def get(self, index):
        """
        This method will return the node present at the index given as an argument to the method. 
        
        There are two edge cases for this method:
        1. Whent the index is less than 0.
        2. When the index is greater than the length of the DLL

        If we simply iterate over the DLL the time complexity is O(n). There is a more efficient way to do it. 
        We will check if the index is less than the mid point of the list. If yes, we will iterate over from the 
        head to the mid of the list. If index is greater than the mid of the list, we will iterate over backwards
        from the tail of the list. This way the time complexity will be O(n)/2. 
        
        """
        # Case where the index is invalid
        if index < 0 or index >= self.length:
            return None

        # Case where the index is valid

        # Case where the index is less than half the length of the DLL
        if index < self.length/2:
            temp = self.head        
            for _ in range(index):
                temp = temp.next
        
        # Case where the index is greater than half the length of DLL
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev

        return temp
    
    def set_value(self, index, value):
        """
        This method will get the node at the "index" and will change the value of the node to "value". 
        
        To get the correct node, "get()" method is used. If the "get()" method returns a node, "set_value()" 
        method will return True. If "get()" method returns None, "set_value()" method will return False. 
         
        """
        # Get the node at the 'index'
        temp = self.get(index)

        # If the 'temp' variable is None
        if temp is None:
            return False
        else:
            temp.value = value
            return True
        
    def insert(self, index, value):
        """
        This method will insert a node of the 'value' at the given 'index'.
        To insert a node at the beginning, 'prepend()' method will be used. To insert a node at the end 'append()'
        method will be used. 
         
        The edge cases for this method are as follows:
        1. When the index is either less than zero or greater than the length of the list.
        
        """
        # Case: index is less than zero or greater than the length of the list
        if index < 0 or index > self.length:
            return False
        # Case: index is 0
        elif index == 0:
            return self.prepend(value)
        # Case: index is equal to length of the list
        elif index == self.length:
            return self.append(value)
        # Case: index value in the list
        else:
            # Create a new node
            new_node = Node(value)

            # Get node before desired index
            before = self.get(index-1)
            after = before.next

            # Assign the new node pointers to before and after
            new_node.prev = before
            new_node.next = after

            # Assign the before and after node pointers to new_node
            before.next = new_node
            after.prev = new_node

            self.length += 1

            return True


    def print_list(self):
        """
        Method for priting the contents of the doubly linked list

        This method will iterate over the list and print the value of each node. The time complexity is O(n)

        """
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next


if __name__ == "__main__":
    my_doubly_linked_list = DoublyLinkedList(1)
    my_doubly_linked_list.append(3)


    print('DLL before insert():')
    my_doubly_linked_list.print_list()


    my_doubly_linked_list.insert(1,2)

    print('\nDLL after insert(2) in middle:')
    my_doubly_linked_list.print_list()


    my_doubly_linked_list.insert(0,0)

    print('\nDLL after insert(0) at beginning:')
    my_doubly_linked_list.print_list()


    my_doubly_linked_list.insert(4,4)

    print('\nDLL after insert(4) at end:')
    my_doubly_linked_list.print_list()
