#!/usr/bin/python3

"""This function is for craeting an object from a json file"""
import json


def load_from_json_file(filename):
    """This function is for craeting an object from a json file"""

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
