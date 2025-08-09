
"""This function is for craeting an object from a json file"""
import sys
import os

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

if __name__ == "__main__":
    filename = "add_item.json"
    arg_list = []
    arg_list.extend(sys.argv[1:])
    save_to_json_file(arg_list, filename)
    load_from_json_file(filename)
