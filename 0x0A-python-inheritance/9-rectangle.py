#!/usr/bin/python3
"""
This module contain a class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A Rectangle class

    Instantiation with width and height

    Args:
        width (int): positive integer
        height (int): postive integer
    """
    def __init__(self, width, height):
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)

    def area(self):
        """
            function to claculate the Rectangle area

        Returns:
            int: the Rectangle area
        """
        return (self.__width * self.__height)
