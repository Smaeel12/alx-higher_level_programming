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
        '''
        to retrieve the private size of the square
        '''
        return self._Square__size

    @size.setter
    def size(self, value):
        '''
        to set the private size of the square
        '''
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        '''
        Method that return the current square area
        '''
        return self._Square__size * self._Square__size

    def my_print(self):
        '''
        prints in stdout the square with the character #
        '''
        if self._Square__size == 0:
            print()
        else:
            for i in range(0, self._Square__size):
                print("#" * self._Square__size)
