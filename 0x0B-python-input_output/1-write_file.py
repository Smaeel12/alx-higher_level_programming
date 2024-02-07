#!/usr/bin/python3
"""
This module contain a function that writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)

    Args:
        filename (str): the relative path to the file.
        text (str): a string to write

    Returns:
        int:  the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
