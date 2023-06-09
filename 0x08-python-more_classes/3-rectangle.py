#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """A class representing a rectangle."""

    @property
    def width(self):
        """Getter method for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle (default: 0).
            height (int): The height of the rectangle (default: 0).
        """
        self.__height = height
        self.__width = width

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """__str__ magic method"""
        pattern = (f"#" * self.__width + "\n") * self.__height
        return pattern.rstrip("\n")

    def __repr__(self):
        """__repr__ magic method"""
        return f"<3-rectangle.Rectangle object at 0x7f92a75a2eb8>"
