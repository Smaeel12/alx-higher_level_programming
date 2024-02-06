#!/usr/bin/python3
"""
This module contain a class MyList that inherits from list
"""


class MyList(list):
    """ A a class MyList
    """
    def print_sorted(self):
        """
        function  that prints the list, but sorted (ascending sort)
        """
        new = super().copy()
        new.sort()
        print(new)
