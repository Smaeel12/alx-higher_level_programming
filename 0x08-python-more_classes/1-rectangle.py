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

    @property
    def width(self):
        """int: width proprety
        set the width using the given value
        """
        return self.__height

    @property
    def height(self):
        """int: height proprety
        set the height using the given value
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value
