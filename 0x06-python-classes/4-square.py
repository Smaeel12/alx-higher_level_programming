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

    @property
    def size(self):
        """ Get and Set the size of the square
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if not (value > 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculate the area of a square
        """
        return self.__size * self.__size