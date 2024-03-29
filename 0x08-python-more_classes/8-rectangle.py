#!/usr/bin/python3
""" This module an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """ Defines a rectangle
    The __init__ method to initialize the height and width
    Args:
        height(int, optional): Width parameter. Defaults to 0.
        width(int, optional): Height parameter. Defaults to 0.
    Attributes:
        height(int): Width private instance attribute
        width(int): Height private instance attribute
        number_of_instances(int): Public class attribute
        print_symbol(int): Public class attribute used
            as symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ method to print the rectangle with the character #
        Return:
            str: empty string if width or height is equal to 0
                otherwise print the rectangle with the character #
        """
        if self.__height != 0 and self.__width != 0:
            for c in range(self.__height):
                for r in range(self.__width):
                    print(self.print_symbol, end='')
                if c < self.__height - 1:
                    print()
        return ''

    def __repr__(self):
        """ method to return a string representation of the rectangle
        Return:
            str: return a string
        """
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

    def __del__(self):
        """ method to print a string Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """int: width proprety
        """
        return self.__width

    @property
    def height(self):
        """int: height proprety
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ Set the height using the given value

        Attributes:
            value(int): The width of the rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ Set the width using the given value

        Attributes:
            value(int): The height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Public instance method that returns the rectangle area
        Return:
            int: rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Public instance method that returns the rectangle perimeter
        Return:
            int: if width or height is equal to 0, return 0
                otherwise rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
