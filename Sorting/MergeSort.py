"""

This file has implementation of merge sort. 
This implementation is done in object oriented style as there is a helper function used.

"""


class SortedMerge:
    def __init__(self):
        self.combined = []

    def _merge(self, list1: list, list2: list) -> list:
        """
        Helper function.

        This function will be used to combine the two already sorted lists.

        list1: Sorted list 1
        list2: Sorted list 2

        return: Combined sorted list

        """
        # We need to iterate over the two lists. This can be done in python using "for-loop" and
        # "len()" function. But, this is not possible in other languages without first knowing
        # The length of the list.

        # Hence, for sake of maintaining consistency in implementaion, we will use "while-loop" instead.

        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                self.combined.append(list1[i])
                # Increment i
                i += 1
            elif list2[j] < list1[i]:
                self.combined.append(list2[j])
                # Increment j
                j += 1

        # Special case where length of list 1 is greater than length of list 2
        while i < len(list1):
            self.combined.append(list1[i])
            i += 1

        # Special case where length of list 2 is greater than length of list 1
        while j < len(list2):
            self.combined.append(list2[j])
            j += 1

        return self.combined


if __name__ == "__main__":
    merge_sort = SortedMerge()
    print(merge_sort._merge([1, 3, 7, 8], [2, 4, 5, 6]))
