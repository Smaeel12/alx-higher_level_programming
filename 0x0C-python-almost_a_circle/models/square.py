#!/usr/bin/python3
""" This module contain a square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ the class constructor
        Args:
            size (int): the size of square.
            x (int, optional): x value. Defaults to 0.
            y (int, optional): y value. Defaults to 0.
            id (int, optional): id value. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ the string representation of the square class
        """
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """ the size property
        """
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """ method to update rectangle class attributes
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if args:
            self.id = args[0]
            self.size = args[1] if 1 < len(args) else self.__size
            self.x = args[2] if 2 < len(args) else self.x
            self.y = args[3] if 3 < len(args) else self.y
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ The dictionary representation of a Square
        Returns:
            dict: dictionary representation
        """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
