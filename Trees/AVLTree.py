"""
This file contains the implementation of AVL trees. 
The theory behind this implementation can be found in the link(s) listed below. 

For understanding the problem with BST:
https://www.datacamp.com/tutorial/avl-tree?dc_referrer=https%3A%2F%2Fwww.google.com%2F

The implementation is also taken from the same link. 
"""

# Define Node class
class Node:
    """
    This class defines the Node of the tree. 
    Compared to BST, only 'parent' is different which points to the parent node of the present node
    """
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 1

    # Method for finding the left height of the tree
    def left_height(self):
        return 0 if self.left is None else self.left.height
    
    # Method to return the right side height of the tree
    def right_height(self):
        return 0 if self.right is None else self.right.height
    
    # Method to find the balance factor at Node
    def balance_factor(self):
        return self.left_height() - self.right_height()
    
    # Method to find the tree height at the present node
    # At the node, tree height is same as self.height
    def update_height(self):
        # The heigth of the node is always more than the height of the children.
        self.height = 1 + max(self.left_height() + self.right_height())
    """
    The following methods set_left() and set_right() are used instead of changing the 
    self.left and self.right directly, because, when we do rotation, it is also required
    to update the parent of the rotated node and height of the tree.
    
    """
    # Method to set the node as the left node 
    def set_left(self, node):
        # Set the node as the left node
        self.left = node
        if node is not None:
            self.parent = self # Set the current node as the parent.
        # Update the height of the tree
        self.update_height()
    
    # Method to set the given node as the right node
    def set_right(self, node):
        # Set the given node as the right node 
        self.right = node
        # If the node is not none, set the current node as a parent
        if node is not None:
            self.parent = self
        # Update the height of the tree
        self.update_height()
    
    # Method to check if the node is the left node.
    # The method will return the boolen True or False.  
    def is_left_child(self):
        return self.parent is not None and self.parent.left == self
    
    # Method to check if the node is the right node.
    # The method will return the boolen True or False
    def is_right_child(self):
        return self.parent is not None and self.parent.right == self
    
class AVLTree:
    """
    Class to initialize a AVL tree whith the root pointing to 'None' in the bginning
    
    The class also contains various methods to rotate the tree left, righ, rebalance, etc. 
    
    """
    def __init__(self):
        self.root = None

    def rotate_left(self, a):
        """
        This method will rotate the tree aroun the node 'a'. """


    if __name__ == "__main__":
        pass

