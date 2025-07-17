#!/usr/bin/python3
def isLower(c):
    if ord(c) not in range(ord('a', ord('z') + 1)):
        return False
    else:
        print(f"{c} is lower")
        return True
