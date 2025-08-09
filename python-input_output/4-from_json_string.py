#!/usr/bin/python3

"""
This function is for making a string json to an object
"""
import json


def from_json_string(my_str):
    """This function is for making a string json to an object"""
    objectifed_json = json.loads(my_str)
    return objectifed_json
