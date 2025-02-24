"""
This file implements an insertion sort algorithm.
The worst case time complexity for the insertion sort is O(n^2). The best case is when you have
a sorted or almost sorted list. In that case the time complexity is O(n).

"""


def insertionSort(my_lst: list) -> list:
    """
    Function to implement insertion sort.

    input:
    my_list: List input (unsorted).

    returns:
    my_list (sorted)

    """
    # Start iterating over the list from the first element of the list
    for i in range(1, len(my_lst)):

        # Assign variable 'temp' to the value at index 'i' and 'j' to the index 'i-1'
        temp = my_lst[i]
        j = i - 1

        # While loop to swith the places of the elements if the value of 'temp' is less than value at index 'j'
        # and as long as 'j' is greater than '-1'.
        # This is a special case when only elements at positions 0 and 1 need to be sorted.
        # The below loop will run until the value at 'i' (temp) is reached to correct position in the
        # list
        while temp < my_lst[j] and j > -1:

            my_lst[j + 1] = my_lst[j]
            my_lst[j] = temp
            j -= 1

    return my_lst


if __name__ == "__main__":
    some_lst = [4, 2, 6, 5, 1, 3]
    print("List before sort: ", some_lst)
    print("List after bubble sort: ", insertionSort(some_lst))
