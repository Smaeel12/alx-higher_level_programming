#!/usr/bin/python3
"""
    This module contain a function that prints My name is
        <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name function that prints My name is <first name> <last name>

    Args:
        first_name(str): First parameter. First name.
        last_name(str): Second parameter. Last name.

    Raises:
        TypeError: Exception if arguments aren't string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
