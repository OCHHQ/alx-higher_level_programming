#!/usr/bin/python3
"""4-square module"""


class Square:
    """Square class with private size attribute"""

    def __init__(self, size=0):
        """Initialize Square with a private size attribute"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute the area of the square"""
        return self.__size ** 2

