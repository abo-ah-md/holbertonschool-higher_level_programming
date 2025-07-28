#!/usr/bin/python3

'''
This module is for creating a rectangle class
'''


class Rectangle:
    """
    A minimal class representing a Rectangle.
    This class currently
    """
    def __init__(self, width=0, height=0):
        """this is an init for the Rectangle class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """this is an getter for the Rectangle class """
        return self.__width

    @width.setter
    def width(self, value):
        """this is an setter for the Rectangle class """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """this is an getter for the Rectangle class """
        return self.__height

    @height.setter
    def height(selfl, value):
        """this is an setter for the Rectangle class """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        selfl.__height = value

    def area(self):
        """this is a perimeter calculate method for the Rectangle class """
        if self.width <= 0 or self.height <= 0:
            return 0
        else:
            return self.height * self.width

    def perimeter(self):
        """this is a perimeter calculate method for the Rectangle class """
        if self.width <= 0 or self.height <= 0:
            return 0
        else:
            return (self.height * 2) + (self.width * 2)

    def __str__(self):
        """this is how to print for the Rectangle class """
        if self.width <= 0 or self.height <= 0:
            return ""
        else:
            lines = []
            for _ in range(self.height):
                lines.append("#" * self.width)
        return "\n".join(lines)
