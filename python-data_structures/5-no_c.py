#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if my_string[i] == "c":
                my_string[i] = ""
        if my_string[i] == "C":
                my_string[i] = ""
        