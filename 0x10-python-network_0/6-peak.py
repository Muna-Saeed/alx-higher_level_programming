#!/usr/bin/python3
"""script for finding peak in list of ints
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # If the mid element is greater than its right neighbor, move left
            high = mid
        else:
            # If the mid element is < or = to its right neighbor, move right
            low = mid + 1

    # At the end of the loop, low and high will be pointing to the peak element
    return list_of_integers[low]
