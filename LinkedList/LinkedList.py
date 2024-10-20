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
        self.tail.next = (
            None  # Without this line, the tail will keep pointing to removed element.
        )
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
        if (
            self.head is None or self.length == 0
        ):  # In reality either one of these conditions is enough.
            self.head = new_node
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
        temp = self.head  # Make a temporary variable pointing to the head
        self.head = self.head.next
        temp.next = None  # The pointer of the removed node should point to "None".
        self.length -= 1

        # Case where there is only one element in the linked list
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def LLGet(self, index):
        """
        This method will get the value of the node present at the given index.

        Technically, there are no indexes in the linked list. So, we will create a "temp" variable and iterate it
        till the value of the index is reached with a for loop. Once the for loop is finished, we will print the value
        of that node.

        Following edge cases should be considered:
        1. When the user enters index -1
        2. When the user enters index larger than the list length.

        """

        # Case where index is -1 or greater than the length of the list
        if index < 0 or index >= self.length:
            return None

        # Case where the index is within range

        temp = self.head  # Create a temp variable pointing to the head

        for _ in range(index):  # Iterate over the list till index is reached
            temp = temp.next

        return temp  # Return the value of temp

    def LLSet_value(self, index, value):
        """
        This method will set the new value for the node using "index" and "value" arguments

        Following edge cases should be considered:
        1. When the user enters index -1
        2. When the user enters index larger than the list length.

        Since the edge cases are same as "LLGet" method, we can use the "LLGet" method as a part of this method to
        make the code easier.

        The implementation of this method without "LLGet" is as shown below.

        '''
        if index < 0 or index >= self.length:
            return None
        temp = self.head # Create a temp variable pointing to the head
        for _ in range(index): # Iterate over the list till index is reached
            temp = temp.next
        temp.value = value
        return True
        '''

        """

        temp = self.LLGet(index=index)  # Get the value of the node at index

        if temp is not None:  # If the "temp" is not returned as None
            temp.value = value  # Change the value of node
            return True
        return False  # If "temp" is None, return False.

    def LLInsert(self, index, value):
        """
        This method will insert a new node at the given index position.

        For this method, the first two edge cases for the index are the same, i.e. the index is out of bounds.
        The third and forth edge cases are important.
        1. When the user enters index -1
        2. When the user enters index larger than the list length.
        3. When we want to insert a node in the beginning, we can simply use the "LLPrepend" method.
        4. When we want to inset the node at the end, we can simply use the "LLAppend" method.

        The difference between "insert" and "set" is, when we "set", we just change the value of the existing node. When
        we "insert", we insert a new node and make linked list longer.

        To get the value of the index, where the node is to be inserted, we can use "LLGet(index-1)".
        """

        # Condition where the list is empty, there is no item to pop.
        if index < 0 or index > self.length:
            return False

        # Case where the node is to be inserted at the end
        if index == self.length:
            return self.LLAppend(value)

        # Case where the node has to be inserted in the beginning
        if index == 0:
            return self.LLPrepend(value)

        # Case where the node has to be inserted in the middle somewhere
        # Create a new node with value
        new_node = Node(val=value)

        # Get the value of the node before the required index and assign it to a variable temp
        temp = self.LLGet(index - 1)

        # Set the pointer of the new node to where the temp is pointing
        new_node.next = temp.next

        # Set the pointer of the temp to new node
        temp.next = new_node

        # Increase the length of list by 1
        self.length += 1

        return True

    def LLprint(self):
        """
        Method to print all elements in linked list

        """
        temp = self.head  # Set a temporary pointer to the head of the node

        while temp is not None:  # As long as pointer has some value
            print(temp.value)  # Print the value of the pointer
            temp = temp.next  # Set the pointer value to next memory location


if __name__ == "__main__":

    my_linked_list = LinkedList(1)
    my_linked_list.LLAppend(3)

    print("LL before insert():")
    my_linked_list.LLprint()

    my_linked_list.LLInsert(1, 2)

    print("\nLL after insert(2) in middle:")
    my_linked_list.LLprint()

    my_linked_list.LLInsert(0, 0)

    print("\nLL after insert(0) at beginning:")
    my_linked_list.LLprint()

    my_linked_list.LLInsert(4, 4)

    print("\nLL after insert(4) at end:")
    my_linked_list.LLprint()
