#!/usr/bin/python3
"""
This module contain a class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A Square class

    Instantiation with size

    Args:
        size (int): the square size
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator('size', size)
        self.__size = size

    def __str__(self):
        return '[Square] {}/{}'.format(self.__size, self.__size)

    def area(self):
        """
            function to calculate the square area

        Returns:
            int: the square area
        """
        return (self.__size ** 2)
