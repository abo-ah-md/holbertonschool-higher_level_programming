# Python Input/Output Project

## 💡 Overview

This project is part of the holbertonschool-higher_level_programming curriculum. It focuses on **Python input/output operations**, file manipulation, and working with JSON serialization/deserialization. The tasks are designed to practice real-world skills essential for software engineering, with all scripts compatible and tested under Ubuntu 20.04 LTS Python 3.8.5.

## 📚 Resources

- [7.2. Reading and Writing Files](https://intranet.hbtn.io/rltoken/n4cEqOMm5PdqDE26lyWcDw)
- [8.7. Predefined Clean-up Actions](https://intranet.hbtn.io/rltoken/PhUB_UH5Ry2tGGK2VGJNGA)
- [Dive Into Python 3: Chapter 11. Files](https://intranet.hbtn.io/rltoken/ciGk1flXa0Pbn8gv-x1FxQ) *(until “11.4 Binary Files”)*
- [JSON encoder and decoder](https://intranet.hbtn.io/rltoken/0p1V5yvlnt3iCTE0DWV2Cg)
- [Learn to Program 8: Reading/Writing Files](https://intranet.hbtn.io/rltoken/zjejIRFH-ZgDaLLp6BWYnA)
- [Automate the Boring Stuff With Python](https://intranet.hbtn.io/rltoken/AOiShF_tqAawS_pKaiX51w) *(ch. 8 p. 180-183 and ch. 14 p. 326-333)*
- [sys package](https://intranet.hbtn.io/rltoken/nIuRQWNy4mJBiqtKHgvJSw)

## 🎯 Learning Objectives

By completing this project you will be able to:

- Explain why Python programming is awesome
- Open, read, and write to files
- Understand and use the `with` statement for file handling
- Read a file line by line, move the cursor, and ensure files are properly closed
- Understand what JSON is, serialization, and deserialization
- Convert Python data structures to JSON strings and vice versa
- Handle command-line arguments in Python scripts

## 📝 Requirements

- All code must be executed/interpreted with Python 3.8.5 on Ubuntu 20.04 LTS
- **Editors:** vi, vim, emacs only
- All files end with a newline and start with `#!/usr/bin/python3`
- **README.md** at the project root is **mandatory**
- Code must pass `pycodestyle` (version 2.7.*)
- All files executable; length may be tested with `wc`
- Docs required for modules, classes, and functions (real sentences, checked for length)
- Test cases must reside in `/tests`, use `.txt` extension, and run with `python3 -m doctest ./tests/*`
- Encourage collaborative edge case testing

## 📁 Directory Structure

    python-input_output/
        ├── 0-read_file.py
        ├── 1-write_file.py
        ├── 2-append_write.py
        ├── 3-to_json_string.py
        ├── 4-from_json_string.py
        ├── 5-save_to_json_file.py
        ├── 6-load_from_json_file.py
        ├── 7-add_item.py
        ├── 8-class_to_json.py
        ├── 9-student.py
        ├── 10-student.py
        ├── 11-student.py
        ├── 12-pascal_triangle.py
        ├── main.py
        └── README.md

## 🚀 Tasks Overview

- **0. Read file**: Prints text file contents (*use `with` statement, no imports/exceptions*)
- **1. Write to a file**: Write string to file, returns number of chars, overwrites if exists
- **2. Append to a file**: Appends string at end, returns number of chars added
- **3. To JSON string**: Returns JSON representation of an object (string)
- **4. From JSON string to Object**: Parses JSON string into Python object
- **5. Save Object to a file**: Serializes object to JSON and writes to file
- **6. Create object from JSON file**: Reads JSON from file, returns Python object
- **7. Load, add, save**: Adds CLI arguments to list and saves as JSON in `add_item.json`
- **8. Class to JSON**: Converts object attributes (simple types) to dict for serialization
- **9. Student to JSON**: Class `Student`, uses `.to_json()` to represent attributes in dict
- **10. Student to JSON with filter**: `Student.to_json(attrs)` can filter by list of attributes
- **11. Student to disk and reload**: Implements serialization & deserialization for `Student`
- **12. Pascal's Triangle**: Returns Pascal’s triangle as a list of lists

## ✒️ Documentation & Style

- Write **docstrings** for every module/class/function: full sentences, explain purpose
- Check documentation length/conformance as per objectives
- Follow pycodestyle, ensure clean/executable code

## 🌐 Running Tests

Place all `.txt` test files inside `/tests`:
```
python3 -m doctest ./tests/*
```

## 🏆 Project Best Practices
- Use **with** statements for file operations
- Avoid unnecessary imports; rely on built-ins unless needed for JSON (`import json`)
- Collaborate on edge cases in testing folders
- Ensure all new code is properly documented and formatted

---

**Author:** _Your Name / Holberton School_  
**Repository:** [holbertonschool-higher_level_programming](https://github.com/abo-ah-md/holbertonschool-higher_level_programming)  
**Directory:** `/python-input_output/`

