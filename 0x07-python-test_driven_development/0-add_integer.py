#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds 2 integers.

    Args:
        a (int): First integer.
        b (int, optional): Second integer. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    """
    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
