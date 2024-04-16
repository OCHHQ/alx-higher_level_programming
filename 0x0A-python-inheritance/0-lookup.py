#!/usr/bin/python3

""" module for lookup method """

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the names of attributes and methods of the object.

    """
    return dir(obj)
