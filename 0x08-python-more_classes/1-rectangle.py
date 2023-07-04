#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """A class representing a rectangle."""

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
                Args:
            value: The new width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
                Args:
            value: The new height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle (default: 0).
            height (int): The height of the rectangle (default: 0).
        """
        self.__height = height
        self.__width = width
