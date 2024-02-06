#!/usr/bin/python3
"""
This module contain a class MyInt
"""


class MyInt(int):
    """ A class MyInt
    instiated with number

    Args:
        num (int): a number
    """
    def __init__(self, num):
        self.num = num

    def __str__(self):
        """
            string representation of an instance

            Returns:
                str: an “informal” string representation
        """
        return '{}'.format(self.num)

    def __eq__(self, other):
        """
            defines the functionality of the equality operator (==).

            Args:
                other (int): the right-hand operand
        """
        if self.num == other:
            return False
        return True

    def __ne__(self, other):
        """
            defines the functionality of the inequality operator (!=).
            Args:
                other (int): the right-hand operand
        """
        if self.num == other:
            return True
        return False
