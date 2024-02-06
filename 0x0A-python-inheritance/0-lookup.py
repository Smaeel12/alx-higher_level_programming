#!/usr/bin/python3
"""
Lookup module contain a function to print the available attributes and methodes
"""


def lookup(obj):
    """
    function that returns the list of available attributes
    and methods of an object

    Args:
        obj (object): an object

    Returns:
        list: attributes and methods of an object
    """
    return dir(obj)
