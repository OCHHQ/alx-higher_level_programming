#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance with size, x, y, and id."""
        super().__init__(size, size, x, y, id)  # call super class constructor with size as width and height

    def __str__(self):
        """Return the string representation of Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
