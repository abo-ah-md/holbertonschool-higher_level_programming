#!/usr/bin/python3

"""
this module for creating an abc subclass
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    the Animal abstracted class contains sound abstracted method
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
