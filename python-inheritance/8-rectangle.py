#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
this module for creating a class
"""


class Rectangle(BaseGeometry):
    """
    rectangle is a sub class of BaseGeometry
    """

    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
