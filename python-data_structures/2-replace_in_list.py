#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx + 1 > len(my_list):
        return my_list
    else:
        my_list[idx] = element
        new_list = my_list
        return new_list
