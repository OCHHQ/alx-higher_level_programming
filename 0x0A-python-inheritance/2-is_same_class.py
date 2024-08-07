#!/usr/bin/python3
""" Module for is_same_class """

def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class; False otherwise.


    """
    return type(obj) == a_class
