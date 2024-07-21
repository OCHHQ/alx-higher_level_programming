#!/usr/bin/python3

"""
File: 101-add_attribute.py
Desc: This module contains a single function
Author: Tsion
Date Created:Dec 14 2022
"""


def add_attribute(obj, att, value):
    """
    Adds a new attribute to an object if it’s possible.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
