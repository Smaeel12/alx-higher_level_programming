# -*- coding: utf-8 -*-
""" a module that defines a empty class """


class Square():
    """ an empty class Square that defines a square
    Attributes:
        size (int, optional): The size of a square
    """
    def __init__(self, size=0):
        """ Initialize a new instance
        Args:
            size (int): The size of a square
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calculate the area of a square
        """
        return self.__size * self.__size