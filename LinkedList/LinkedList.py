"""
This program will create a linked list and will have methods associated with linked list like append, pop, etc. 

"""


class Node:
    """
    Class for creating a single node.

    Constructor will take the value of the node as an input and since, this is a single node,
    the pointer for the next memory location is set to "None"

    """

    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    """
    Class where the actual linked list is created.

    """

    def __init__(self, val):
        """
        Class constructor for linked list.

        Please note that, the 'head' and the 'next' point to the node iteslf and
        not to the value and memory location

        """
        new_node = Node(val)  # Take the input value and make a node
        self.head = new_node  # Set the head to the new node
        self.tail = new_node  # Set the tail of linked list to the current node
        self.length = 1  # Set the length of the linked list to 1

    def LLAppend(self, val):
        """
        Method to append new values in linked list

        The time complexity for this operation is O(1)
        Constant time because, we do not need to iterate over list. We know where is the last element.
        """
        node_val = Node(val)  # Create a new node.

        if (
            self.head == None
        ):  # Condition where the list is an empty. New node becomes the only element in the list.
            self.head = node_val
            self.tail = node_val

        self.tail.next = node_val  # The pointer of the last element points to new node
        self.tail = node_val  # The entire tail itself points to new node
        self.length += 1  # Increase the length of the linked list by 1
        return True

    def LLPop(self):
        """
        This method will remove the last item from the linked list.

        This is a much complicated operation than append, because, we need to iterate over list.
        Time complexity for this operation is O(n)

        There are three edge cases for pop.

        1. If the list is empty
        2. If the list has two or more items
        3. If the list has only one item

        """
        # Check if the list is empty and return None if it is empty
        # This is the case, when the list is empty (no items in the list)
        if self.head is None:
            return None

        # The following code is for the condition where there are two or more items in the list
        # Create two variables pointing to head in the beginning
        temp = self.head
        pre = self.head

        # Iterate over the list with "temp" and "pre" should be one node behind "temp"
        while temp.next is not None:
            pre = temp
            temp = temp.next  # This condition will remain true until last node

        self.tail = pre
        self.tail.next = None # Without this line, the tail will keep pointing to removed element.
        self.length -= 1

        # If there is only one item in the list, the line above for decreasing the length by 1 will be executed
        # After that we need to point the head and tail to None.
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp
    
    def LLPrepend(self, val):
        """
        This method will add a node at the beginning of the linked list. 
        
        The following edge cases should be considered:
        1. When the linked list is empty
        2. When the list has one or more elements
        
        """
        # Create a new node
        new_node = Node(val)

        # Condition where the list is empty
        if self.head is None or self.length == 0: # In reality either one of these conditions is enough.
            self.head =  new_node
            self.tail = new_node
            # Adding one element in an empty list does not actually change the length of the list.
            # Hence we are not going to increase "self.length" here. 

        # Condition where the list has one or more elements
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True
    def LLPopfirst(self):
        """
        
        This method will pop the first item from the linked list.
        
        Following edge cases should be considered
        
        1. When the linked list is empty. i.e both head and tail are None
        2. When the linked list has only one item
        
        """
        # Condition where the list is empty, there is no item to pop. 
        if self.head == None or self.length == 0:
            return None
        
        # Condition where there are one or more elements in the list
        temp = self.head # Make a temporary variable pointing to the head 
        self.head = self.head.next
        temp.next = None # The pointer of the removed node should point to "None".
        self.length -= 1

        # Case where there is only one element in the linked list
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp
        
        
    def printLL(self):
        """
        Method to print all elements in linked list

        """
        temp = self.head  # Set a temporary pointer to the head of the node

        while temp is not None:  # As long as pointer has some value
            print(temp.value)  # Print the value of the pointer
            temp = temp.next  # Set the pointer value to next memory location


if __name__ == "__main__":

    my_linked_list = LinkedList(2)
    my_linked_list.LLAppend(3)

    print('Before prepend():')
    print('----------------')
    print('Head:', my_linked_list.head.value)
    print('Tail:', my_linked_list.tail.value)
    print('Length:', my_linked_list.length, '\n')
    print('Linked List:')
    my_linked_list.printLL()


    my_linked_list.LLPrepend(1)


    print('\n\nAfter prepend():')
    print('---------------')
    print('Head:', my_linked_list.head.value)
    print('Tail:', my_linked_list.tail.value)
    print('Length:', my_linked_list.length, '\n')
    print('Linked List:')
    my_linked_list.printLL()
