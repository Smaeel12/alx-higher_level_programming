#!/usr/bin/python3
"""
    This module contain a function that adds 2 integers.
    Usage example:
        >>> add_integer(13, 14)
"""


def add_integer(a, b=98):
    """
    add_integer function that adds 2 integers.
    """
    try:
        if type(a) in (int, float):
            a = int(a)
        else:
            raise
    except Exception:
        raise TypeError("a must be an integer")
    try:
        if type(b) in (int, float):
            b = int(b)
        else:
            raise
    except Exception:
        raise TypeError("b must be an integer")
    return a + b
