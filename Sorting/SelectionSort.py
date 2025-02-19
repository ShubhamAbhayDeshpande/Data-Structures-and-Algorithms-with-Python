"""
This file contais implementation of simple Selection Sort Algorithm. 

The implementation is similar to Bubble Sort. But, instead of taking into consideration tha values 
of the indexes, we sort using index iteself. The use of two for-loops is common in both methods. 

"""


def selectionSort(my_lst: list):
    """
    Function for implementation selection sort.

    my_lst: Some unsorted list of length 'n'

    """

    # Defining first for loop to iterate over the list
    for i in range(len(my_lst) - 1):
        min_idx = i
        # Second for loop to compare elements at all indexes with min_idx
        for j in range(i + 1, len(my_lst)):
            # Condition where value at min_idx is greater than value next to it, change the min_idx
            if my_lst[j] < my_lst[min_idx]:
                min_idx = j

        # After finding the true min_idx, swap the value with idx. This only works if i and min_idx are
        # different values
        if i != min_idx:
            temp = my_lst[i]
            my_lst[i] = my_lst[min_idx]
            my_lst[min_idx] = temp

    return my_lst


if __name__ == "__main__":
    some_lst = [4, 2, 6, 5, 1, 3]
    print("List before sort: ", some_lst)
    print("List after bubble sort: ", selectionSort(some_lst))
