#!/usr/bin/python3

"""
This function is for Reading a file
"""


def read_file(filename=""):
    """
This function is for Reading a file
    """

    with open(filename) as file:
        data = file.read()
        print(data,end="")
