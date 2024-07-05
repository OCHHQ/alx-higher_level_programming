#!/usr/bin/python3
"""
Module to find a peak in a list of unsorted integers.

This module contains a function `find_peak` that recursively searches
for a peak in an unsorted list of integers using a binary search approach.

Example:
    print(find_peak([1, 2, 4, 6, 3]))  # Output: 6
    print(find_peak([4, 2, 1, 2, 3, 1]))  # Output: 3
    print(find_peak([2, 2, 2]))  # Output: 2
    print(find_peak([]))  # Output: None
    print(find_peak([-2, -4, 2, 1]))  # Output: 2
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 4
"""

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of integers to search.

    Returns:
        int or None: Peak element if found, None if list is empty.
    """
    if not list_of_integers:
        return None

    def find_peak_recursive(arr, low, high):
        """
        Recursively find a peak in the list using binary search.

        Args:
            arr (list): List of integers to search.
            low (int): Lower index of the search range.
            high (int): Upper index of the search range.

        Returns:
            int: Peak element found.
        """
        if low == high:
            return arr[low]

        mid = (low + high) // 2

        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
            return arr[mid]
        elif mid > 0 and arr[mid] < arr[mid - 1]:
            return find_peak_recursive(arr, low, mid - 1)
        else:
            return find_peak_recursive(arr, mid + 1, high)

    return find_peak_recursive(list_of_integers, 0, len(list_of_integers) - 1)
