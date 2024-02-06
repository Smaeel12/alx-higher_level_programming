#!/usr/bin/python3
"""
This module contain a function to check class inheritance
"""


def inherits_from(obj, a_class):
    """
    function to check class inheritance

    Args:
        obj (object): an object
        a_class (object): an object type

    Returns:
        bool: True if the object is an instance of a class that
            inherited (directly or indirectly) from the specified
            class; otherwise False.
    """
    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
