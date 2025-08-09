#!/usr/bin/python3
"""This function is for craeting json from class dict"""

import json
def class_to_json(obj):
    return json.dumps(__dict__(obj))
