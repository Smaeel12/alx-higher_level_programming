#!/usr/bin/python3
"""
This module contain a function to check object instances
"""


def is_kind_of_class(obj, a_class):
    """
    function to check object instances and inheritance

    Args:
        obj (object): an object
        a_class (object): an object type

    Returns:
        bool: True if the object is an instance of,
            or if the object is an instance of a class that
            inherited from, the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
