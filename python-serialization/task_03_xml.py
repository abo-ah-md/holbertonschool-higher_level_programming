#!/usr/bin/python3

''' This module for CSV serelize and deserize to json'''

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    try:

        root = Et.Element("data")
        for key, value in data.items:
            child = ET.subElement(root,key)
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
            data[child.tag] = child.text
        return data
