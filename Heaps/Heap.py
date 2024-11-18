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
        return (index - 1) // 2

    def _swap(self, index1, index2):
        """
        This third helper method will be used to swap the values of the two indices
        of the list given as inputs.

        """
        self.heap[index1] = self.heap[index1] + self.heap[index2]
        self.heap[index2] = self.heap[index1] - self.heap[index2]
        self.heap[index1] = self.heap[index1] - self.heap[index2]


if __name__ == "__main__":
    my_heap = Heap()
    my_heap.heap.append(5)
    my_heap.heap.append(10)
    print(my_heap.heap)
    my_heap._swap(0, 1)
    print(my_heap.heap)
