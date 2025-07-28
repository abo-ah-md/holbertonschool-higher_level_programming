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
    def __init__(self, size=0, position=(0, 0)):
        """this is an init for the square class """
        self.size = size
        self.position = position

    @property
    def size(self):
        """this is a getter of the private size property """

        return self.__size

    @property
    def position(self):
        """this is a getter of the private size property """

        return self.__position

    @size.setter
    def size(self, value):
        """this is a setter of the private size property """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in range(len(value)):
                if not isinstance(value[i], int) or \
                   value[i] < 0 or len(value) != 2:
                    raise TypeError("position must be a \
                    tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """this is an init dor the square class """

        return self.__size ** 2

    def my_print(self):
        """this method will print # in sqaure shape in addition to postion"""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] != 0:
                print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                if self.__position[0] != 0:
                    print(" " * self.position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
