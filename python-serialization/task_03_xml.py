#!/usr/bin/python3
''' This module for XML serialize and deserialize to dict '''
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    # Create root
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)
        item.set("type", type(value).__name__)
    

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    result = {}
    for elem in root:
        value_type = elem.get("type", "str")
        text = elem.text
        

        if value_type == "int":
            value = int(text)
        elif value_type == "float":
            value = float(text)
        elif value_type == "bool":
            value = text.lower() == "true"
        else:
            value = text
        
        result[elem.tag] = value
    
    return result



if __name__ == "__main__":
    data = {
        "name": "Abdullah",
        "age": 25,
        "pi": 3.14159,
        "is_student": False
    }
    
    serialize_to_xml(data, "data.xml")
    print("Serialized XML saved to data.xml ✅")
    
    loaded_data = deserialize_from_xml("data.xml")
    print("Deserialized data:", loaded_data)
