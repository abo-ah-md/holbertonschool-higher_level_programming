#!/usr/bin/python3

'''
this module is  adds the functionality to serialize 
a Python dictionary to a JSON file and 
deserialize the JSON file to recreate 
the Python Dictionary.
'''
import json


def serialize_and_save_to_file(data, filename):
    json.dumps(data,filename)

def load_and_deserialize(filename):
    with open(filename,"r",encoding="utf-8") as file:
        json.loads(file)
