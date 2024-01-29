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
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    def __str__(self):
        """ method to print the rectangle with the character #
        Return:
            str: empty string if width or height is equal to 0
                otherwise print the rectangle with the character #
        """
        if self.__height != 0 or self.__width != 0:
            for c in range(self.__height):
                for r in range(self.__width):
                    print('#', end='')
                if c < self.__height - 1:
                    print()
        return ''

    @property
    def width(self):
        """int: width proprety
        set the width using to the given value
        """
        return self.__height

    @property
    def height(self):
        """int: height proprety
        set the height using to the given value
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Public instance method that returns the rectangle area
        Return:
            int: rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Public instance method that returns the rectangle perimeter
        Return:
            int: if width or height is equal to 0, return 0
                otherwise rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
