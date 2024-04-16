#!/usr/bin/python3
""" module for mylist class """

class MyList(list):
    """
    A subclass of list with additional methods.
    """
    def print_sorted(self):
        """
        Prints the list in sorted order (ascending).
        """
        sorted_list = sorted(self)
