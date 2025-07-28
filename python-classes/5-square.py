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

    @property
    def size(self):
        """this is a getter of the private size property """
        return self.__size

    @size.setter
    def size(self, value):
        """this is a setter of the private size property """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """this is an init dor the square class """
        return self.__size ** 2

    def my_print(self):
        """this method will print # in sqaure shape"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
