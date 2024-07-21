#!/usr/bin/python3
"""
File: 7-base_geometry.py
Desc: Module with class; BaseGeometry
Author: Tsion
"""


class BaseGeometry:
    """
    Representation of the class
    """
    def area(self):
        """
        Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
