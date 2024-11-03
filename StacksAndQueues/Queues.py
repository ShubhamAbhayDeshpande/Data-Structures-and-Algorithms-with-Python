"""
This file contais basic implementation and methods associated with queues 

"""


# Defining a node in Queue
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


# Defining the class for constructing queue
class Queue:
    def __init__(self, value=None):
        """
        This is a basic class constructor which will define where the node will be defined and where
        'first' and 'last' variables for a node point to.

        """
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        """
        Method to print all the elements in queue

        """
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        """
        This method will add new values to the queue.
        The value will be converted to a node which will be added to the queue from the 'last' position. Because,
        the queue works on FIFO principle.

        The edge case is the one where the queue is empty the beginning.

        """
        # Make a new node with the given value
        new_node = Node(value)

        # If the queue is empty in the beginning.
        if self.first is None:
            self.first = new_node
            self.last = new_node

        # If the queue has one more elements
        else:
            self.last.next = new_node
            self.last = new_node

        # Increase the length of the queue by 1
        self.length += 1

    def dequeue(self):
        """
        This method will remove an element from the queue.

        The values will be removed from the first element according to FIFO principle.

        The edge case is when the queue is empty. In that case, the method will return 'None' When the queue has
        only one element, we remove that element and assign the first and last variable to 'None'.

        """
        # When the queue is empty in the beginning
        if self.length == 0:
            return None

        # The first is element is assigned to 'temp' variable
        temp = self.first

        # When the queue has only one element
        if self.length == 1:
            self.first = None
            self.last = None

        # When the queue has two or more elements
        else:
            self.first = self.first.next
            temp.next = None

        # Decrease the length of the queue by one
        self.length -= 1

        # Return 'temp' with the value of the variable
        return temp


if __name__ == "__main__":
    my_queue = Queue(1)
    print("elements in queue: ")
    my_queue.print_queue()
    my_queue.enqueue(7)
    print("Queue after adding one element")
    my_queue.print_queue()
    my_queue.dequeue()
    print("Queue after removing one elmenet")
    my_queue.print_queue()
    