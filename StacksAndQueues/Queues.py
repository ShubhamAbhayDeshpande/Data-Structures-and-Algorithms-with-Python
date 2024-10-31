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


if __name__ == "__main__":
    my_queue = Queue(1)
    print("elements in queue: ")
    my_queue.print_queue()
