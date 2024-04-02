#!/usr/bin/python3
"""3-square module"""


class Square:
    """Square class with private size attribute"""

    def __init__(self, size=0):
        """Initialize Square with a private size attribute"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Compute the area of the square"""
        return self.__size ** 2

