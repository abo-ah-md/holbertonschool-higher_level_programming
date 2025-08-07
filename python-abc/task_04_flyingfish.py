#!/usr/bin/python3

"""
this module for creating an abc subclass
"""
class Fish():
    """
    this calss extends some of the methods in list with printed message
    """

    def swim(self):
        print("The fish is swimming")
    def habitat(self):
        print("The fish lives in water")
class Bird():
    """
    this calss extends some of the methods in list with printed message
    """

    def fly(self):
        print("The bird is flying")
    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish,Bird):
    """
    this calss extends some of the methods in list with printed message
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")
    
    def habitat(self):
        print("The flying fish lives both in water and the sky!")
