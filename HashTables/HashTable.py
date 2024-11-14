"""
This file contains implementation of hash tables and various methods associated with the hash
table.

"""


# Defining the constructor for the hash class
class HashTable:
    def __init__(self, size=7):
        """
        Create an instance of the class hash table.
        The class accepts the value for the size of the hash table. By default it is 7.

        The constructor will also create a data map with the size equal to the size of the
        value given as an input.

        """
        self.data_map = [None] * size

    def __hash(self, key):
        """
        Method to actually hash the values given to the class.

        This method will accept the 'key' to store in the hash table as an input.

        To avoid confusion with the existing '__hash__()' method method in python, "name mangeling"
        is used in this method. This indicates that the method is for internal class use only and
        should not be modified or used by external user. This is not a foolproof solution and a
        determined user can still access and modify the method.

        """
        # Define the variable to store the hash address
        my_hash = 0

        # Loop over the values in the provided 'key'
        for letters in key:

            # In the following formula, hash value for each letter in key will be found
            # ord() function returns ASCI vlaue for each letter
            # We are adding it to last used hash address (my_hash)
            # Multiplying it by 23 because it is a prime number(we can use any prime number here).
            # Using modulo operartion with length of the hash table because, for example if the
            # used data map length is 7, when we take a modulo with this number, we get remainder
            # which is in between 0 and 6. That is exactly our address space.
            my_hash = (my_hash + ord(letters) * 23) % len(self.data_map)

        # return the hash value
        return my_hash

    def print_table(self):
        """
        Method to print all the values in the hash table along with their respective indexes
        in the table.

        """
        for i, val in enumerate(self.data_map):
            print(i, " : ", val)


if __name__ == "__main__":
    my_hash_table = HashTable()
    my_hash_table.print_table()
