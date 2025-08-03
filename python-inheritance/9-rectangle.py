#!/usr/bin/python3

"""
this module for creating a class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectangle is a sub class of BaseGeometry
    """

    def __init__(self, width, height):
        """
        rectangle is a sub class of BaseGeometry
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        print(f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        """
        calculating area of rectangle
        """
        return self.__height * self.__width
