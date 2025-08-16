#!/usr/bin/python3
''' This module for XML serialize and deserialize to dict '''

import xml.etree.ElementTree as ET

def datatype_checker(value):
    if value is None:
        return None

    # Boolean check
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False

    # Integer check
    try:
        return int(value)
    except ValueError:
        pass

    # Float check
    try:
        return float(value)
    except ValueError:
        pass

    # Fallback: string
    return value


def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception as e:
        print(f"Serialization failed: {e}")
        return False


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data = {}

        for child in root:
            correct_data_type = datatype_checker(child.text)
            data[child.tag] = correct_data_type
        return data
    except Exception as e:
        print(f"Deserialization failed: {e}")
        return None
