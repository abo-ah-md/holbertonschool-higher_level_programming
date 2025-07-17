#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i)  in range(ord('a'), ord('z') + 1):
            print(chr(i + 32))
