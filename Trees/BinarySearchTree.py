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
            if temp == new_node:
                return False

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


if __name__ == "__main__":
    my_tree = BinarySearchTree()
    my_tree.insert(2)
    print("Root: ", my_tree.root.value)
    my_tree.insert(3)
    my_tree.insert(1)
    print("left: ", my_tree.root.left.value)
    print("right: ", my_tree.root.right.value)
