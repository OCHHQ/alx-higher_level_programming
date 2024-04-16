#!/usr/bin/python3

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the names of attributes and methods of the object.

    Example:
        >>> lookup([1, 2, 3])
    """
    return dir(obj)
