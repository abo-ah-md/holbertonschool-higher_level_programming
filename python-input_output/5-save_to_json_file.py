#!/usr/bin/python3

"""
This function is for writing an object json representaion to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """This function is for writing an object json representaion to a file"""
    try:
        jsonifed_obj = json.dumps(my_obj)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(jsonifed_obj)
    except (TypeError, PermissionError) as e:
        print(f"[Error] {e}")
