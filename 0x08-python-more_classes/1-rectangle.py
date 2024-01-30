#!/usr/bin/python3
""" This module an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """ Defines a rectangle
    The __init__ method to initialize the height and width
    Args:
        height(int, optional): Width parameter. Defaults to 0.
        width(int, optional): Height parameter. Defaults to 0.
    Attributes:
        height(int): Width private instance attribute
        width(int): Height private instance attribute
        number_of_instances(int): Public class attribute
        print_symbol(int): Public class attribute used
            as symbol for string representation
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: width proprety
        """
        return self.__width

    @property
    def height(self):
        """int: height proprety
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ Set the height using the given value

        Attributes:
            value(int): The width of the rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ Set the width using the given value

        Attributes:
            value(int): The height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
