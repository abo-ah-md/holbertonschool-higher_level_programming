#!/usr/bin/python3

"""
this module for creating an abc subclass
"""
class VerboseList(list):
    """
    this calss extends some of the methods in list with printed message
    """


    def extend(self,iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def append(self, elem):
        super().append(elem)
        print(f"Added [{elem}] to the list.")

    def remove(self,elem):
        if elem not in self:
            return
        print(f"Removed [{elem}] from the list.")
        super().remove(elem)

    def pop(self,elem = -1):
        print(f"Popped [{self[elem]}] from the list.")        
        return super().pop(elem)
        
