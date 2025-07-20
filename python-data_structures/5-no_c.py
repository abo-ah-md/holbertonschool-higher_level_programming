#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if ord(my_string[i]) == ord("c"):
                my_string[i] = ""
        if ord(my_string[i]) == ord("C"):
                my_string[i] = ""
        