#!/usr/bin/python3
"""
This module contain an empty class BaseGeometry.
"""


class BaseGeometry:
    """ A geometry class """

    def area(self):
        """
            function that raises an Exception error

        Raises:
                Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            function that validates value

        Args:
            name (str): the name
            value (int): the value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
