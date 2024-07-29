#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" a module that defines a empty class """


class Square():
    """ an empty class Square that defines a square
    Attributes:
        size (int, optional): The size of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a new instance
        Args:
            size (int): The size of a square
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

        if not (isinstance(position, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """ Get and Set the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculate the area of a square
        """
        return self.__size * self.__size

    def my_print(self):
        """ Prints in stdout the square with the character # and spaces
        """
        if not (self.__size):
            print()
        if self.__position[1] >= 0:
            print("\n" * self.__position[1], end='')
            for _ in range(self.__size):
                print(' ' * self.__position[0], end='')
                print("#" * self.__size, end='')
                print()
