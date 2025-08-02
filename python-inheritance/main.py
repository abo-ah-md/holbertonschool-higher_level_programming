#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.ia("my_int", 12)
bg.ia("width", 89)

try:
    bg.ia("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.ia("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.ia("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
