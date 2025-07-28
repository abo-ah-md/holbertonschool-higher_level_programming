#!/usr/bin/python3

'''
This module is for creating a rectangle class
'''


class Rectangle:
    """
    A minimal class representing a Rectangle.
    This class currently
    """
    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """this is an init for the Rectangle class """
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """this is an init for the Rectangle class """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
    def height(self, value):
        """this is an setter for the Rectangle class """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """this is an init for the Rectangle class """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.height * rect_1.width
        area2 = rect_2.height * rect_2.width

        if area1 == area2:
            return rect_1
        elif area1 > area2:
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """this is how to print for the Rectangle class """
        if self.width <= 0 or self.height <= 0:
            return ""
        else:
            lines = []
            for _ in range(self.height):
                lines.append(f"{str(self.print_symbol)}" * self.width)
        return "\n".join(lines)

    def __repr__(self):
        """this is how to print for the Rectangle class """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
