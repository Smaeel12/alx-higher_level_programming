#!/usr/bin/python3
"""
    This module contain a function that prints a square with the character #.
"""


def print_square(size):
    """
    function that prints a square with the character #.

    Args:
        size(int): size of the square

    Raises:
        TypeError: Exception if size is not integer
        ValueError: Exception if size is less than 0
    """
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")

    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        print('#'*int(size))
