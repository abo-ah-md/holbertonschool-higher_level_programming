#!/usr/bin/python3

"""
This function is for returning if obect is an exact instanse of calss
"""


def inherits_from(obj, a_class):
    """
    This function is for returning if obect is an exact instanse of calss
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
