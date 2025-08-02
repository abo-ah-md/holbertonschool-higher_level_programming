#!/usr/bin/python3

"""
this module for creating  class MyList that inherits from list
"""


class MyList(list):
    """
    this module for creating  class MyList that inherits from list
    """

    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self, *args):
        return self.sort(*args)
