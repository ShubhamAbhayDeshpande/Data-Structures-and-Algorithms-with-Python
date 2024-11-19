"""
This file contains implementation of heap along with some of the helper methods
to find the left and right index of the node and to swap the node values. 

"""


class Heap:
    def __init__(self):
        """
        The constructor of the heap only implements a empty list which will be
        used for storing all the values in the heap.

        """
        self.heap = []

    def _left_child(self, index):
        """
        First helper method.

        This method will be used for finding the left child of the index given
        as an input to this method.

        """
        return 2 * index + 1

    def _right_child(self, index):
        """
        Second helper method

        This helper method will be used for finding the right child of the index
        given as an input to this method.

        """
        return 2 * index + 2

    def _parent(self, index):
        """
        Helper method to find the parent of the node present at the given index.

        """
        return (index - 1) // 2

    def _swap(self, index1, index2):
        """
        This third helper method will be used to swap the values of the two indices
        of the list given as inputs.

        """
        self.heap[index1] = self.heap[index1] + self.heap[index2]
        self.heap[index2] = self.heap[index1] - self.heap[index2]
        self.heap[index1] = self.heap[index1] - self.heap[index2]

    # Method to insert a new element in heap
    def insert(self, value):
        """
        This method will insert the new 'value' in the heap and assign that value
        correct position.

        """
        # Append the new value to the heap
        self.heap.append(value)
        # Assign the index of the new element to a variable called 'current'
        current = len(self.heap) - 1

        # Make a while loop to assign the new element correct position
        # The while loop will run until the 'current' is not at the top of the list
        # Or until the value of the element at index 'current' is no longer greater than its parent.

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


if __name__ == "__main__":
    my_heap = Heap()
    my_heap.insert(99)
    my_heap.insert(72)
    my_heap.insert(61)
    my_heap.insert(58)
    print("Heap before inserting element:")
    print(my_heap.heap)
    print("Heap after inserting the element:")
    my_heap.insert(100)
    my_heap.insert(75)
    print(my_heap.heap)
