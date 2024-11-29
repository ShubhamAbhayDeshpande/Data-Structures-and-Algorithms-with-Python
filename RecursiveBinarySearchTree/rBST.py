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

    # Helper recursive methods for recursive methods
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
    
    def __delete_node(self, current_node, value):
        """
        This is the recursive delete method called by the 'r_delete()' method. 
        
        The method will accept two paramenters, current_node and the value. 
        If the value of the current node is less than or greater than the "value", this mehtod will
        be called recursively. If the current node value and "value" is same, there are four possible
        cases, 
        1. When there are no sub-trees to current node
        2. When the sub-tree is present only on the right side of the current node
        3. When the sub-tree is present only on the left side of the current node
        4. When the sub-trees are present on both left and right side of the current node. 
        
        In the 4th case, we need another helper method called "deleteMinimum()" which will find and 
        delete minimum element in sub-tree and is written below.
        
        """
        # If the current node value becomes None, we can return that value to call stack
        if current_node is None:
            return None
        # If the current node value is less than the value, call recursive instance on left side of tree
        if current_node.value < value:
            current_node.right = self.__delete_node(current_node.left, value)
        # If the current node value is greater than the value, call recursive instance on right side of tree
        elif current_node.value > value:
            current_node.left = self.__delete_node(current_node.right, value)
        # If the current node value and value are same, do the following.
        else:
            # We need to find if the node is a leef node.
            if current_node.left is None and current_node.right is None:
                return None
            # If the node exists on the left side of the node we want to delete
            elif current_node.left is None:
                return current_node.right
            # If the node exists only on the right side of the node we want to delete
            elif current_node.right is None:
                return current_node.left
            # If the nodes exists on both sides of the nodes we want to delete
            else:
                # Find the smallest element on the right sub-tree
                sub_tree_min = self.min_value(current_node.right)
                # Change the vlaue of the current node to sub_tree_min
                current_node.value = sub_tree_min
                # Delete the sub_tree_min node from the tree
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node
    
    # Helper method to find the minimum value in any sub-tree. This method will be used for the recursive delete.
    def min_value(self, current_node):
        """
        This method will keep going on the left of the current node in sub-tree till we have 
        current_node.left as None. After that we return current_node.value as the minimum value.
        
        """
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value # We return value of the node here, because that is what we need in recursive delete method.
    
    def r_contains(self, value):
        """
        This is the method which will be called by the instance of the class. It will use the helper
        __r_contains() method.

        """
        return self.__r_contains(self.root, value)

    def r_insert(self, value):
        """
        This method calls the __r_insert() method recursively.

        There is only one edge case in this: When the tree is empty. In that case, we will assign the
        root to the new node.
        """
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def delete_node(self, value):
        """
        This is the main delete method which will be used by the instances of this class. 
        It will recursively call '__delete_node()' method which is implemented above. 
        
        There is only one boundary condition for this method:
        1. If the tree is empty, there is no element to delete, hence return None. 
        
        """
        if self.root is None:
            return None
        self.__delete_node(self.root, value)


if __name__ == "__main__":

    def check(expect, actual, message):
        print(message)
        print("EXPECTED:", expect)
        print("RETURNED:", actual)
        print("PASS" if expect == actual else "FAIL", "\n")


    # test_delete_node_no_children
    print("\n----- Test: Delete node with no children -----\n")
    bst = rBinarySearchTree()
    values = [5, 3, 8]
    for v in values:
        print("Inserting value:", v)
        bst.r_insert(v)
    bst.delete_node(3)
    check(None, bst.root.left, "Left child of root after deleting 3:")


    # test_delete_node_only_left_child
    print("\n----- Test: Delete node with only left child -----\n")
    bst = rBinarySearchTree()
    values = [5, 3, 8, 1]
    for v in values:
        print("Inserting value:", v)
        bst.r_insert(v)
    bst.delete_node(3)
    check(1, bst.root.left.value, "Left child of root after deleting 3:")


    # test_delete_node_only_right_child
    print("\n----- Test: Delete node with only right child -----\n")
    bst = rBinarySearchTree()
    values = [5, 3, 8, 9]
    for v in values:
        print("Inserting value:", v)
        bst.r_insert(v)
    bst.delete_node(8)
    check(9, bst.root.right.value, "Right child of root after deleting 8:")


    # test_delete_node_two_children
    print("\n----- Test: Delete node with two children -----\n")
    bst = rBinarySearchTree()
    values = [5, 3, 8, 1, 4, 7, 9]
    for v in values:
        print("Inserting value:", v)
        bst.r_insert(v)
    bst.delete_node(3)
    check(4, bst.root.left.value, "Left child of root after deleting 3:")


    # test_delete_root
    print("\n----- Test: Delete root -----\n")
    bst = rBinarySearchTree()
    values = [5, 3, 8]
    for v in values:
        print("Inserting value:", v)
        bst.r_insert(v)
    bst.delete_node(5)
    check(8, bst.root.value, "Root value after deleting 5:")


    # test_delete_non_existent_node
    print("\n----- Test: Attempt to delete a non-existent node -----\n")
    bst = rBinarySearchTree()
    values = [5, 3, 8]
    for v in values:
        print("Inserting value:", v)
        bst.r_insert(v)
    original_root_value = bst.root.value
    bst.delete_node(10)
    check(original_root_value, bst.root.value, "Root value after attempting to delete 10:")
