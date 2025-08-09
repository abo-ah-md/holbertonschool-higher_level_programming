#!/usr/bin/python3

"""This function is for craeting an object from a json file"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == "__main__":
    arg_list = []
    for arg in sys.argv:
        arg_list.append(arg)
    save_to_json_file(arg_list,"add_item.json")
    load_from_json_file("add_item.json")