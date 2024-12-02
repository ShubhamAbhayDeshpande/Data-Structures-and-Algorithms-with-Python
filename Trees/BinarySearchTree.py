"""
This file contains the implementation of Binary Search Tree 

"""


class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        """
        This is the constructor for the BST.
        Unlike LL or DLL, we can initialize a BST with a 'none' value. This is called making an empty tree.

        """
        self.root = None

    def insert(self, value):
        """
        This method will insert new values in the BST. Depending on the values of the root node.
        There are two edge cases when using the insert method.
        1. When the tree is empty: Insert the new node value as a root value and end the program.
        2. When the new node value is already present in the tree: This is a repetition. This is not allowed in BST.

        """
        # Create a new node
        new_node = Node(value)

        # Case 1: if the tree is empty, i.e. root == none, make new node as root and return True
        if self.root is None:
            self.root = new_node
            return True

        # Assign temp variable to the root
        temp = self.root

        # Make a while loop to iterate over tree
        while True:
            # Case 2: If the value of the new node is same as the temp, return false, as repetition is not allowed.
            if temp.value == new_node.value:
                raise ValueError(
                    "The value is already present in the BST. Repetition of value is not allowed."
                )

            # If the value of the new node is less than the temp, either add the new node on the left or check if there are other
            # nodes present on the left side of temp.
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left

            # If the value of the new node is greater than the temp, either add the new node on the right side of the temp or check
            # if other nodes are present on the left side of temp
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right

    def contains(self, value):
        """
        This method will check if the 'value' is present in the tree. If the method return True, the
        value is present in tree. If method return False, the value is not present in the tree.

        The edge cases for this are as follows:

        1. When the tree is empty.

        """
        # Case where the tree is empty
        if self.root is None:
            return False

        # Case where the tree is not empty
        # Create a variable 'temp' to point to the root
        temp = self.root

        # The loop will run until the temp value is turned to 'None'. Meaning the
        # the 'value' is not present in the tree.
        while temp is not None:
            # If the value is less than the 'temp.value' search on the left side of the tree
            if temp.value > value:
                temp = temp.left
            # If the value is greater than the 'temp.value' search on the right side of the tree
            elif temp.value < value:
                temp = temp.right
            # If the value is same as temp.value, return True
            else:
                return True
        # If the 'while' loop is exited, the value is not present in the tree. Return 'False'
        return False

    def BFS(self):
        """
        BFS stands for Breadth First Search.

        It is a way of going through the binary search tree and add all the elements in a list.

        This method will return a list containing all the elements in the BST.

        """
        # Assign the root to current node
        current_node = self.root

        # Make a temporary queue and a result
        queue = []
        result = []

        # Append the queue with the current node at the beginning
        queue.append(current_node)

        # While the length of the queue is not zero
        while len(queue) > 0:
            # pop the node at zero position in queue
            current_node = queue.pop(0)
            # Append the value of the poped node to the result
            result.append(current_node.value)
            # If there is a left and right child to the current node, append those values in queue
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        # Return the 'result' list which contains all the node values.
        return result

    def dfs_pre_order(self):
        """
        This is a depth first search approach to finding all the values in a BST.
        It is implemented using recursion.
        """
        # A list to store all the node values.
        result = []

        # A recursive function to collect all the node values.
        def traverse(current_node):
            """This is the recursive function which will be called in itself multiple times."""
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        # Call the recursive function on the root node
        traverse(self.root)

        # return result
        return result


if __name__ == "__main__":
    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print(my_tree.dfs_pre_order())
