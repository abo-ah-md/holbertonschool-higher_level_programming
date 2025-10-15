# Python - Serialization

## Introduction

Welcome to our exploration of **marshaling** and **serialization**, two fundamental concepts in computer science that enable efficient storage and transmission of data. This project will guide you through transforming and communicating data between different parts of a system, or even across systems. By completing these exercises, you will develop both your understanding and your hands-on skills in modern data handling scenarios.

---

## Table of Contents

- [What is Marshaling?](#what-is-marshaling)
- [What is Serialization?](#what-is-serialization)
- [Learning Objectives](#learning-objectives)
- [Project Tasks](#project-tasks)
  - [0. Basic Serialization (JSON)](#0-basic-serialization-json)
  - [1. Pickling Custom Classes](#1-pickling-custom-classes)
  - [2. Converting CSV Data to JSON Format](#2-converting-csv-data-to-json-format)
  - [3. Serializing and Deserializing with XML](#3-serializing-and-deserializing-with-xml)
- [Resources](#resources)
- [Repository Structure](#repository-structure)

---

## What is Marshaling?

**Marshaling** is the process of transforming memory objects into a format that can be stored or transmitted over a network (often a binary format). This is vital for tasks like remote procedure calls, where objects need to be represented in a standard way across diverse computing platforms.

---

## What is Serialization?

**Serialization** takes structured data (like objects or dictionaries) and converts it to a format suitable for saving to a file or sending over a network, with the goal of preserving the object’s state for later restoration. Serialization is essential for **data persistence, distributed systems, and software interoperability.**

---

## Learning Objectives

- **Describe** the differences and similarities between marshaling and serialization
- **Implement** practical serialization tasks using modern Python techniques
- **Apply** serialization in web apps, databases, and network service contexts
- **Evaluate** performance and trade-offs of different serialization formats: JSON, XML, and binary (pickle)

---

## Project Tasks

### 0. Basic Serialization (JSON)
**File:** `task_00_basic_serialization.py`

- Implement:
  - `serialize_and_save_to_file(data, filename)`: Serializes a Python dictionary and saves it as JSON
  - `load_and_deserialize(filename)`: Loads and deserializes JSON data from a file back into a dictionary

**Usage Example:**

```
from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

data_to_serialize = {
"name": "John Doe",
"age": 30,
"city": "New York"
}
serialize_and_save_to_file(data_to_serialize, 'data.json')
deserialized_data = load_and_deserialize('data.json')
print(deserialized_data)

Output: {'name': 'John Doe', 'age': 30, 'city': 'New York'}
```


---

### 1. Pickling Custom Classes
**File:** `task_01_pickle.py`

- Define a class `CustomObject` with attributes `name`, `age`, `is_student`
- Implement:
  - `serialize(self, filename)`: Serializes object using `pickle`
  - `@classmethod deserialize(cls, filename)`: Loads object from pickle file
  - `display(self)`: Prints human-readable object details

**Sample usage:**

```
obj = CustomObject(name="John", age=25, is_student=True)
obj.serialize("object.pkl")
new_obj = CustomObject.deserialize("object.pkl")
new_obj.display()

Output:
Name: John
Age: 25
Is Student: True
```

---

### 2. Converting CSV Data to JSON Format
**File:** `task_02_csv.py`

- Implement `convert_csv_to_json(csv_filename)`
  - Reads CSV, converts to list of dicts, writes to `data.json` (handles file errors)

**Example dataset (`data.csv`):**

```
name,age,city
John,28,New York
Alice,24,Los Angeles
Bob,22,Chicago
Eve,30,San Francisco
```

**After running:**
```
[
{"name": "John", "age": "28", "city": "New York"},
{"name": "Alice", "age": "24", "city": "Los Angeles"},
{"name": "Bob", "age": "22", "city": "Chicago"},
{"name": "Eve", "age": "30", "city": "San Francisco"}
]
```

---

### 3. Serializing and Deserializing with XML
**File:** `task_03_xml.py`

- Implement:
  - `serialize_to_xml(dictionary, filename)`: Serializes a dict into XML
  - `deserialize_from_xml(filename)`: Loads XML and builds a dict

**Example (XML representation):**
```
<data> <name>John</name> <age>28</age> <city>New York</city> </data> ``` *Note: All XML values are strings—type conversions may be needed when consuming the data.*
```
Resources
Real Python: Serialization

Working With JSON Data in Python

Python’s pickle documentation

Corey Schafer on Pickle

CSV to JSON in Python

Python XML ElementTree Guide

Socket Programming Guide

Repository Structure
task_00_basic_serialization.py – Basic JSON serialization

task_01_pickle.py – Pickle serialization of custom classes

task_02_csv.py – CSV to JSON converter

task_03_xml.py – XML serialization/deserialization

data.csv, data.json, data.xml, object.pkl – Sample data files

main.py – Example script/test runner
