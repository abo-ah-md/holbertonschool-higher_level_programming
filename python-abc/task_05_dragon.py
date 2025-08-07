#!/usr/bin/python3

"""
This module creates a Dragon class using mixins for added behavior.
"""


class SwimMixin:
    """
    This mixin adds swimming behavior.
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    This mixin adds flying behavior.
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon that can swim, fly, and roar.
    """
    def roar(self):
        print("The creature roars!")

draco = Dragon()
draco.swim()  # Outputs: The creature swims!
draco.fly()   # Outputs: The creature flies!
draco.roar()  # Outputs: The dragon roars!
