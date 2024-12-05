"""
This file contais implementation of simple Bubble Sort Algorithm. 

When changing the values of the consecutive variables, technique of changing the values of the
two variables without using a third variable is used. 

"""


def bubbleSort(my_lst: list):
    """
    Functional implementation for bubble sort.

    Input: An unsorted list
    Returns: sorted list

    """
    # The first for loop will run in reverse order. i.e. it will start with the length of the
    # list and run until i = 0. Everytime this loop runs, the value of 'i' will keep on decreasing.
    # In the beginning it will start from length of the list and for second iteration, it will be
    # len(list)-1, for third iteration, len(list)-2 and so on.
    for i in range(len(my_lst) - 1, 0, -1):
        # The second for loop will run from 0 to 'i' and compare the elements at index 'j' and 'j+1'
        # If the value of element at 'j+1' is less than the value of element at 'j', it will switch the elements.
        for j in range(i):
            # If the element at 'j' is greater than the element at 'j+1'
            # Swap the elemnet positions
            if my_lst[j] > my_lst[j + 1]:
                my_lst[j] = my_lst[j] + my_lst[j + 1]
                my_lst[j + 1] = my_lst[j] - my_lst[j + 1]
                my_lst[j] = my_lst[j] - my_lst[j + 1]

    return my_lst


if __name__ == "__main__":
    some_lst = [4, 2, 6, 5, 1, 3]
    print("List before sort: ", some_lst)
    print("List after bubble sort: ", bubbleSort(some_lst))
