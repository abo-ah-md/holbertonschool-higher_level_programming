#!/usr/bin/python3

"""
This function is for writing an object json representaion to a file  
"""
import json


def save_to_json_file(my_obj, filename):
    """This function is for writing an object json representaion to a file  """
    jsonifed_obj = json.dumps(my_obj)
    with open(filename,"w") as file:
        file.write(jsonifed_obj)
