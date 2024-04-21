#!/usr/bin/python3
"""Square by adding the public method def update(self, *args, **kwargs) that assigns attributes"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance with size, x, y, and id."""
        super().__init__(size, size, x, y, id)  # call super class constructor with size as width and height

    @property
    def size(self):
        """Getter method for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign attributes based on the given arguments and keyworded arguments."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
