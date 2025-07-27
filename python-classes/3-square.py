#!/usr/bin/python3

'''
This module is for creating a square class
'''


class Square:
    """
    A minimal class representing a square.
    This class currently has 1 private instanse attribute
    called size and no methods.
    It's essentially a placeholder or a base class for future use.
    """
    def __init__(self, size=0):
        """this is an init for the square class """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """this is an init dor the square class """
        return self.__size ** 2
