#!/usr/bin/python3
def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): Size length of the square.

    Raises:
        TypeError: If size is not an integer or is a float less than 0.
        ValueError: If size is less than 0.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)

