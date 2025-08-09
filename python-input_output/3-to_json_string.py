#!/usr/bin/python3
import json
"""
This function is for writing to aa file
"""


def to_json_string(my_obj):
    """
    This function is for writing to a file
    """
    jsonfied_object = json.dumps(my_obj)
    return jsonfied_object