#!/usr/bin/python3

"""
this module for creating an empty class
"""


class BaseGeometry:
    """
    this module for creating an empty class
    """

    def __init__(self):
        """
        this module for creating an empty class
        """
        pass

    def integer_validator(self, name, value):

        """
        this  for valdating the value 
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """
        this module for creating an empty class
        """
        raise Exception("area() is not implemented")
    