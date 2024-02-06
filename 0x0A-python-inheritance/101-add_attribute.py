#!/usr/bin/python3
"""
This module contain a function that adds a new attribute to an object
"""


def add_attribute(obj, attr, value):
    """
        function that adds a new attribute to an object if it’s possible
    """
    if isinstance(obj, (int, float, str, list, tuple, dict, set)):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
    if not hasattr(obj, attr):
        raise TypeError("can't add new attribute")
