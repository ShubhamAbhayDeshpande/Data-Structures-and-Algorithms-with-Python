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

    def set_item(self, key: str, value: int):
        """
        This method will add a list containing [key, value] at a random address in 'self.data_map'. The index at
        which this list will be added is provided by '__hash()' method. The pseudo code for the same is as follows:

        1. Get index used in self.data_map using __hash() method. Use 'key' as an input to this method.
        2. Check if the index is initialized to 'None'.
        3. If the index is None, initialize it to an empty list
        4. Append a list [key, value] to the index in data_map.

        """
        # Get index
        index = self.__hash(key)

        # check if the index is none
        if self.data_map[index] is None:
            # if yes, initialize empty list
            self.data_map[index] = []
        # Append the list with [key, value]
        self.data_map[index].append([key, value])

    def get_item(self, key):
        """
        This method will provide the 'value' stored in the hash table for the 'key' provided by the user.
        The algo for this method is as follows:

        1. Find the 'index' in the hash table using '__hash()' method.
        2. If, the value at the 'index' is 'None', return 'None'. Meaning, key not present in hash table.
        3. Else, loop through the hash table, using for-loop
        4. If the 0th element of the sub-list matches the 'key', return the 1st element of the sub-list.

        """
        # Get index
        index = self.__hash(key)
        # If the value of data_map is None at index, return None
        if self.data_map[index] is None:
            raise ValueError("Provided 'key' is not present in hash table.")
        # Else, loop throught the list at index and find the value matching key, return value at [1] for key.
        for hash_list in self.data_map[index]:
            if hash_list[0] == key:
                return hash_list[1]

    def keys(self):
        """
        This method will take all the keys present in the hash table, put them in a list and return that list.

        The algo for this method is as follows:

        1. Define empty list
        2. List through all the indexes in the self.data_map
        3. For all the indexes not None, go through the sub-lists, if any
        4. Store the keys in every sub-list to the empty list
        5. Return empty list

        """
        key_list = []
        for index in self.data_map:
            if index is not None:
                for sub_list in index:
                    key_list.append(sub_list[0])
        return key_list

    def print_table(self):
        """
        Method to print all the values in the hash table along with their respective indexes
        in the table.

        """
        for i, val in enumerate(self.data_map):
            print(i, " : ", val)


if __name__ == "__main__":
    my_hash_table = HashTable()
    my_hash_table.set_item("bolts", 100)
    my_hash_table.set_item("washers", 70)
    my_hash_table.set_item("lumber", 80)
    print("testing get method: ", my_hash_table.get_item("washers"), "\n")
    print("list of keys in hash map: ", my_hash_table.keys(), "\n")
    my_hash_table.print_table()
