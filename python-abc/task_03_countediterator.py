#!/usr/bin/python3

"""
this module for creating an abc subclass
"""
class CountedIterator():
    """
    this calss extends some of the methods in list with printed message
    """

    def __init__(self, data):
        self.iterator = iter(data)
        self.counter = 0

    def __next__(self):
        self.counter += 1
        
        return next(self.iterator)
        
    def get_count(self):
        return self.counter
