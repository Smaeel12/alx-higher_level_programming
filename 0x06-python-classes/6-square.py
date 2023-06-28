#!/usr/bin/python3
'''class Square'''


class Square:
    '''
    class Square that defines a square by: (based on 4-square.py)

    attributes:
        Private instance attribute: size

    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
        size must be an integer, otherwise TypeError exception raised
        with the message size must be an integer
        if size is less than 0, ValueError exception raised
        with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Methodes:
        Public instance method:
            def area(self): that returns the current square area
    '''
    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.
        """
        return self._Square__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) or num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = value

    def __init__(self, size=0, position=(0, 0)):
        self._Square__size = size
        self._Square__position = position

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self._Square__size * self._Square__size

    def my_print(self):
        """
        Prints the square using '#' character.
        """
        if self._Square__size == 0:
            print()
        else:
            for i in range(self._Square__position[1]):
                print()
            for i in range(self._Square__size):
                print(" " * self._Square__position[0], end="")
                print("#" * self._Square__size)
