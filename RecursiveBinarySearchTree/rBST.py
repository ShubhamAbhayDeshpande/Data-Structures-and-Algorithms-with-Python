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

    def __r_insert(self, current_node, value):
        """
        This is a recursive method which will be called when inserting a new value in tree.

        The brake condition is when the value of the current node is "None". Then the actual Node with
        value is created. This is then returned to the function call where it will be attached to either
        left or the right pointer of the current_node

        """
        # The brake condition
        if current_node is None:
            return Node(value)
        # Following are the two recursive calls when the value is either smaller or greater than
        # current node value.
        # When the value is less than the current node value
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        # When exiting recursive method call, a final value of the current node will be returned.
        return current_node

    def r_insert(self, value):
        """
        This method calls the __r_insert() method recursively.

        There is only one edge case in this: When the tree is empty. In that case, we will assign the
        root to the new node.
        """
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)


if __name__ == "__main__":

    def check(expect, actual, message):
        print(message)
        print("EXPECTED:", expect)
        print("RETURNED:", actual)
        print("PASS" if expect == actual else "FAIL", "\n")

    print("\n----- Test: Insert into an empty tree -----\n")
    bst = rBinarySearchTree()
    print("Inserting value:", 5)
    bst.r_insert(5)
    check(5, bst.root.value, "Root value after inserting 5:")
    check(None, bst.root.left, "Left child of root:")
    check(None, bst.root.right, "Right child of root:")

    print("\n----- Test: Insert values in ascending order -----\n")
    bst = rBinarySearchTree()
    values = [1, 2, 3, 4, 5]
    for val in values:
        print("Inserting value:", val)
        bst.r_insert(val)

    # Check tree structure
    check(1, bst.root.value, "Root value:")
    check(2, bst.root.right.value, "Right child of root:")
    check(3, bst.root.right.right.value, "Right child of right child of root:")
    check(
        4,
        bst.root.right.right.right.value,
        "Right child's right child's right child of root:",
    )
    check(5, bst.root.right.right.right.right.value, "Fourth right child of root:")

    print("\n----- Test: Insert values in descending order -----\n")
    bst = rBinarySearchTree()
    values = [5, 4, 3, 2, 1]
    for val in values:
        print("Inserting value:", val)
        bst.r_insert(val)

    # Check tree structure
    check(5, bst.root.value, "Root value:")
    check(4, bst.root.left.value, "Left child of root:")
    check(3, bst.root.left.left.value, "Left child of left child of root:")
    check(
        2,
        bst.root.left.left.left.value,
        "Left child's left child's left child of root:",
    )
    check(1, bst.root.left.left.left.left.value, "Fourth left child of root:")

    print("\n----- Test: Insert values in mixed order -----\n")
    bst = rBinarySearchTree()
    values = [3, 1, 4, 5, 2]
    for val in values:
        print("Inserting value:", val)
        bst.r_insert(val)

    # Check tree structure
    check(3, bst.root.value, "Root value:")
    check(1, bst.root.left.value, "Left child of root:")
    check(2, bst.root.left.right.value, "Right child of left child of root:")
    check(4, bst.root.right.value, "Right child of root:")
    check(5, bst.root.right.right.value, "Right child of right child of root:")

    print("\n----- Test: Insert duplicate values -----\n")
    bst = rBinarySearchTree()
    values = [3, 3, 3]
    for val in values:
        print("Inserting value:", val)
        bst.r_insert(val)

    # Check tree structure
    check(3, bst.root.value, "Root value:")
    check(None, bst.root.left, "Left child of root:")
    check(None, bst.root.right, "Right child of root:")
