"""
This file contains implementation of heap along with some of the helper methods
to find the left and right index of the node and to swap the node values. 

The following implementation is for MaxHeap. For MinHeap a different class needs
to be written.

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

    def _sink_down(self, index):
        """
        This helper method is specifically used for the remove() method in heap.

        It is only used when the heap has two or more items and the top most item is removed.
        The method written below is only useful for max heap remove method. For min heap remove,
        please change the comparison signs in if-statements.

        """
        # Set index equal to new variable max_index
        max_index = index

        while True:
            # Find the left and right indices of the index
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            # If the left child is greater than index and left index is less than length of the heap
            # Assign max index to left index
            if (
                left_index < len(self.heap)
                and self.heap[left_index] > self.heap[max_index]
            ):
                max_index = left_index
            if (
                right_index < len(self.heap)
                and self.heap[right_index] > self.heap[max_index]
            ):
                max_index = right_index
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            return True

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

    def remove(self):
        """
        This method will remove the top item of the heap. It doesn't matter if the heap
        is min-heap or a max-heap.

        There are three boundary conditions for this method:
        1. When the heap has no items. Return None
        2. When heap has only one item: return item at index 0
        3. When heap has two or more items: Use "sink-down" method.

        """
        # When the heap is empty
        if len(self.heap) == 0:
            return None

        # When the heap has only one item
        if len(self.heap) == 1:
            return self.heap.pop()

        # When the heap has two or more items
        max_val = self.heap[
            0
        ]  # just assign the max or min value to the variable. Return it later
        # pop() method will by default pop the last value in the list.
        # We assign the last value to the starting index of the list.
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        # Return the max or the min value
        return max_val


if __name__ == "__main__":
    myheap = Heap()
    myheap.insert(95)
    myheap.insert(75)
    myheap.insert(80)
    myheap.insert(55)
    myheap.insert(60)
    myheap.insert(50)
    myheap.insert(65)

    print(myheap.heap)

    myheap.remove()

    print(myheap.heap)

    myheap.remove()

    print(myheap.heap)
