#!/usr/bin/python3

''' This module for xml serelize and deserize to dict'''

import xml.etree.ElementTree as ET


def datatype_checker(value):

    if value is None:
        return None


    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False


    try:
        return int(value)
    except ValueError:
        pass


    try:
        return float(value)
    except ValueError:
        pass


    return value

def serialize_to_xml(dictionary, filename):
    try:

        root = ET.Element("data")
        for key, value in data.items():
            child = ET.SubElement(root,key)
            child.text = str(value)
            tree = ET.ElementTree(root)
        tree.write(filename, encoding= "utf-8", xml_declaration =True)
    except:
        return False

def deserialize_from_xml(filename):

        tree = ET.parse(filename)
        root = tree.getroot()
        data = {}
        
        for child in root :
            correct_data_type = datatype_checker(child.text)
            data[child.tag] = correct_data_type
        return data
