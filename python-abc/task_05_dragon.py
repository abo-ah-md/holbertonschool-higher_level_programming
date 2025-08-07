#!/usr/bin/python3

"""
this module for creating an abc subclass
"""
class SwimMixin():
    """
    this calss extends some of the methods in list with printed message
    """

    def swim(self):
        print("The creature swims!")

class FlyMixin():
    """
    this calss extends some of the methods in list with printed message
    """

    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin,FlyMixin):
    """
    this calss extends some of the methods in list with printed message
    """
    def roar(self):
        print("The creature roar!")
