#!/usr/bin/python3
"""
This module contain a function that check object instance
"""


def is_same_class(obj, a_class):
    """
    function too check a class instance

    Args:
        obj (object): an object
        a_class (object): an object type

    Returns:
        bool: True if the object is an instance; otherwise False.

    """
    return bool(obj.__class__ == a_class)
