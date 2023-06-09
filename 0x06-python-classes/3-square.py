#!/usr/bin/python3
'''class Square'''


class Square:
    '''
    class Square that defines a square by: (based on 2-square.py)

    attributes:
        Private instance attribute: size

    Instantiation with optional size: def __init__(self, size=0):
        size must be an integer, otherwise TypeError exception raised
        with the message size must be an integer
        if size is less than 0, ValueError exception raised
        with the message size must be >= 0
    Methodes:
        Public instance method:
            def area(self): that returns the current square area
    '''
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

    pass
