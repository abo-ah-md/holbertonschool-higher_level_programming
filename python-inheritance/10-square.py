#!/usr/bin/python3

"""
this module for creating a class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square is a sub class of Rectangle
    """

    def __init__(self, size):
        """
        Square is a sub class of Rectangle
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        calculating area of Square
        """
        return self.__size ** 2
