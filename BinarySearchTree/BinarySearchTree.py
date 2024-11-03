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


if __name__ == "__main__":
    my_tree = BinarySearchTree()
    print("Root: ", my_tree.root)
