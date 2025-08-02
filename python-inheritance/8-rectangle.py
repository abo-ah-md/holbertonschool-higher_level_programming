#!/usr/bin/python3

"""
this module for creating a class
"""


class BaseGeometry:
    """
    this module for creating an  class
    """

    def __init__(self):
        """
        this module for creating a class
        """
        pass

    def integer_validator(self, name, value):
        """
        this  for valdating the value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """
        this will give the area later on
        """
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):
    """
    rectangle is a sub class of BaseGeometry
    """

    def __init__(self, width, height):
        super(BaseGeometry).__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
