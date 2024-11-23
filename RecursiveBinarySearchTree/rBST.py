"""
This file contains implemnetation of Binary Search Tree with recursive methods. 

This does not affect the constructor used for the BST. The way we initialize the node and the tree constructor
itself is the same. 

What is changed is the implementation of the methods for "contains()", "insert()" and one additional
"delete()" method. 

"""


# Node class for tree
class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


# Tree class
class rBinarySearchTree:
    def __init__(self):
        """
        This is the constructor for the BST.
        Unlike LL or DLL, we can initialize a BST with a 'none' value. This is called making an empty tree.

        """
        self.root = None

    # Helper recursive method for 'contains()'.
    def __r_contains(self, current_node: any, value: any):
        """
        This is a helper method which will be called in the actual recursive method.
        The brake conditions for the method are as follows:
        1. When the 'current_node' is 'None': return False or raise ValueError.
        2. When the 'value' attribute of the 'current_node' is equal to 'value' input: return True

        If the 'vlaue' is greater than the 'current_node.value', call the same helper method with 'current_node'
        changed to 'current_node.right'.

        If the 'value' is less than the 'current_node.value', call the same helper method with 'current_node'
        changed to 'current_node.left'.
        """
        if current_node is None:
            raise ValueError("The given value is not present in the tree.")
        if current_node.value == value:
            return True
        if current_node.value < value:
            return self.__r_contains(current_node.right, value)
        if current_node.value > value:
            return self.__r_contains(current_node.left, value)

    def r_contains(self, value):
        """
        This is the method which will be called by the instance of the class. It will use the helper
        __r_contains() method.

        """
        return self.__r_contains(self.root, value)

    # Before we can find if the tree contains a certain node or not, we need to insert nodes in tree.
    # Hence, the following method is written. It is a place holder for recursive insert.
    # It will be deleted later.
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


if __name__ == "__main__":
    my_tree = rBinarySearchTree()
    my_tree.insert(2)
    print("Root: ", my_tree.root.value)
    my_tree.insert(3)
    my_tree.insert(1)
    print("left: ", my_tree.root.left.value)
    print("right: ", my_tree.root.right.value)
    print(my_tree.r_contains(9))
