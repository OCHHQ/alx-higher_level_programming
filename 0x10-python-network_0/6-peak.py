#!/usr/bin/python3
"Write a function that finds a peak in a list of unsorted integers."


def find_peak(list_of_integers):
    """ Function to find a peak in a list of unsorted integers """
    if not list_of_integers:
        return None

    def find_peak_recursive(arr, low, high):
        if low == high:
            return arr[low]

        mid = (low + high) // 2

        # Check if the mid element is greater than or equal to its neighbors
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
            return arr[mid]
        elif mid > 0 and arr[mid] < arr[mid - 1]:
            return find_peak_recursive(arr, low, mid - 1)
        else:
            return find_peak_recursive(arr, mid + 1, high)

    return find_peak_recursive(list_of_integers, 0, len(list_of_integers) - 1)
