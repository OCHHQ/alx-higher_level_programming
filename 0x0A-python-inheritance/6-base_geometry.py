#!/usr/bin/python3
"""Module for class of BaseGeometry class base on 5-base_geometry.py"""
class BaseGeometry:
    """
    Base class representing base geometry.

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented".
    """
    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")
