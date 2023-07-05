#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """A class representing a rectangle."""
    __width = None
    __height = None
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        pattern = (f"{self.print_symbol}" * self.__width + "\n")
        * self.__height
        return pattern.rstrip("\n")

    def __repr__(self):
        """__repr__ magic method"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """__del__ magic method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles and return the one
        with the greater or equal area. """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """The square class method creates a square instance
        with equal side lengths."""
        return cls(size, size)
