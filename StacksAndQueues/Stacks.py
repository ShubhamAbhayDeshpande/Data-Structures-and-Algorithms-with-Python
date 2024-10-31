"""
This file contains the constructor and the associated methods with the stacks.

"""


# Defining the node class
class Node:
    """
    The class will take one argument 'val' and will be used to make the nodes
    for a stack

    """

    def __init__(self, val):
        self.value = val
        self.next = None


# Class for stack definition
class Stack:
    """
    Class for stack definition

    """

    def __init__(self, value=None):
        """
        Class constructor for stack.
        Takes only one positional argument

        """
        # Define a new node
        new_node = Node(value)

        # Assign/ Point 'top' variable to new node
        self.top = new_node

        # Point the next variable to 'None'
        self.next = None

        # Set the height of stack to 1
        self.height = 1

    def push(self, value):
        """
        This method will 'push' the new node on top of the existing one in stack.

        The edge cases for this method are as follows:
        1. When there are no nodes in the stack.

        """
        new_node = Node(value)

        # When the stack is empty
        if self.top is None:
            self.top = new_node
        # When there are pre-existing elements in stack
        else:
            new_node.next = self.top
            self.top = new_node
        # Increase stack height by 1
        self.height += 1
        # Optional return statement
        return True

    def pop(self):
        """
        This method will remove the top element in a stack.

        This method does not require any default argument. it will return the node at the top
        The edge case is when the stack is empty. Then this method will retunr None.

        """
        # When the stack is empty
        if self.top is None:
            return None
        # When there are elements present in stack
        else:
            temp = self.top
            self.top = self.top.next
            self.height -= 1
            return temp

    def print_stack(self):
        """
        Method to print the contents of the stack.

        """
        # Create a 'temp' variable and assign it to the top.
        temp = self.top

        # Iterate over the stack until we reach the 'bottom' element.
        while temp is not None:
            print(temp.value)
            temp = temp.next


if __name__ == "__main__":

    my_stack = Stack()
    print("stack before push: ")
    my_stack.print_stack()
    my_stack.push(5)
    print("stack after new element is pushed: ")
    my_stack.print_stack()
    ele = my_stack.pop()
    print("stack after poping last added element: ")
    my_stack.print_stack()
    print("poped out element value: ", ele.value)
