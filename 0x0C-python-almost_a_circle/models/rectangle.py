#!/usr/bin/python3
""" This module contain a rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """ a Rectangle class
    Attributes:
        width (int): private instance attr. the width
        height (int): private instance attr. the height
        x (int): private instance attr. x
        y (int): private instance attr. y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Contructor method
        Args:
            width (int): the width
            height (int): the height
            x (int): x
            y (int): y
            id (int, optional): the id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """ string representation for the class attribute
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        """ The width property
        """
        return self.__width

    @property
    def height(self):
        """ The height property
        """
        return self.__height

    @property
    def x(self):
        """ The x property
        """
        return self.__x

    @property
    def y(self):
        """ The y property
        """
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ method to calculate the rectangle area
        Returns:
            int: the area value of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """ method that prints in stdout the Rectangle
        instance with the character #
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(' ', end="")
            for _ in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """ method to update rectangle class attributes
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if args != ():
            self.id = args[0]
            self.__width = args[1] if 1 < len(args) else self.__width
            self.__height = args[2] if 2 < len(args) else self.__height
            self.__x = args[3] if 3 < len(args) else self.__x
            self.__y = args[4] if 4 < len(args) else self.__y
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ The dictionary representation of a Rectangle
        Returns:
            dict: dictionary representation
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
