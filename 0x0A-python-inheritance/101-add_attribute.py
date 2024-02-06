#!/usr/bin/python3
"""
This module contain a function that adds a new attribute to an object
"""


def add_attribute(obj, attr, value):
    """
        function that adds a new attribute to an object if it’s possible
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
