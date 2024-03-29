#!/usr/bin/python3
"""
This module contain a function that appends a string at the end of a text file
(UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
     a function that appends a string at the end of a text file (UTF8)

    Args:
        filename (str): the relative path to the file.
        text (str): a string to append

    Returns:
        int:  the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
