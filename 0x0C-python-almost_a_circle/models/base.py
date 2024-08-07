#!/usr/bin/python3
"""Create a file named models/base.py"""

class Base:
    """Base class for managing id attribute in all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance with id."""
        if id is not None:
            self.id = id  
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
