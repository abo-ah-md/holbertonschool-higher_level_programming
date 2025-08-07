#!/usr/bin/python3

"""
This module creates a Dragon class using mixins for added behavior.
"""


class SwimMixin:
    """
    This mixin adds swimming behavior.
    """
    def swim(self):
        """
        This mixin adds flying behavior.
        """
        print("The creature swims!")


class FlyMixin:
    """
    This mixin adds flying behavior.
    """
    def fly(self):
        """
        This mixin adds flying behavior.
        """

        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon that can swim, fly, and roar.
    """
    def __init__(self,ability=""):
        """
        This mixin adds flying behavior.
        """
        self.ability = ability

    def abt(self):
        """
        This mixin adds flying behavior.
        """
        print(f"The creature {self.ability}s")
    

    def roar(self):
        """
        This mixin adds flying behavior.
        """
        print("The creature roars!")

if __name__ == "__main__":
    draco = Dragon("drive a clude")
    draco.swim()
    draco.fly()
    draco.roar()
    draco.abt()
