#!/usr/bin/env python3

class CountedIterator():
    """this calss extends some of the methods in list with printed message"""

    def __init__(self, data):
        self.iterator = iter(data)
        self.counter = 0

    def __next__(self):
        try:
            item =  next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
        
    def get_count(self):
        """Return the iterator itself."""
        return self.counter

    def __iter__(self):
        """Return the iterator itself."""
        return self
