# Python - More Classes

## Overview

This project is a deep dive into **Object Oriented Programming (OOP)** in Python. It covers the implementation of various rectangle-related functionalities and reinforces critical OOP concepts— including class vs instance attributes, initialization, data abstraction, encapsulation, and more — through practical exercises.

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
- [Repository Structure](#repository-structure)

---

## Resources

Read or watch for deeper understanding:
- **Object Oriented Programming:**  
  Read everything until the “Inheritance” paragraph (excluded).
- **Object-Oriented Programming:**  
  Focus only on these paragraphs:  
  - General Introduction  
  - First-class Everything  
  - A Minimal Class in Python  
  - Attributes  
  - Methods  
  - The `__init__` Method  
  - Data Abstraction, Data Encapsulation, and Information Hiding  
  - `__str__` and `__repr__` Methods  
  - Public, Protected, and Private Attributes  
  - Destructor  
- [Class and Instance Attributes]()
- [classmethods and staticmethods]()
- [Properties vs. Getters and Setters]()
  - Especially the section: “Public instead of Private Attributes”
- [str vs repr]()

---

## Learning Objectives

By the end of this project you should be able to explain and demonstrate:
- **General Python & OOP:**
  - Why Python programming is awesome
  - What OOP is
  - *First-class everything*
  - What a class is
  - Difference between class, object, and instance
  - What an attribute is
  - Public, protected, private attributes & how to use them
  - `self` usage
  - What a method is
  - Purpose and usage of `__init__`
  - Data abstraction, encapsulation, information hiding
  - What a property is
  - Attribute vs property in Python
  - Pythonic way to write getters and setters
  - `__str__` vs `__repr__` differences and implementations
  - What a class attribute is
  - Difference between object attribute and class attribute
  - What a class method is
  - What a static method is
  - Dynamic creation of attributes for instances
  - Attribute binding to objects and classes
  - Understanding and using `__dict__` of a class/instance
  - How Python searches for attributes
  - Usage of `getattr` function

---

## Requirements

- **General:**
  - Editors: `vi`, `vim`, `emacs`
  - Python3 (version 3.8.5) on Ubuntu 20.04 LTS
  - All files end with a new line
  - Shebang: `#!/usr/bin/python3` as the first line of every file
  - Mandatory `README.md` at the root of the project
  - Code style: `pycodestyle` (version 2.7.*)
  - All files must be executable
  - File lengths tested with `wc`

---

## Tasks

### 0. Simple Rectangle
- Write an empty class `Rectangle`.
- Example output:
```
<class '0-rectangle.Rectangle'>
{}
```

---

### 1. Real Definition of a Rectangle
- Define `Rectangle` with private instance attributes `width` and `height`, with property getters/setters.
- Raise appropriate `TypeError` and `ValueError` for invalid values.
- Initialization via `__init__`.

---

### 2. Area and Perimeter
- Add methods:
- `area()`: returns rectangle area.
- `perimeter()`: returns perimeter, returns `0` if width or height is `0`.

---

### 3. String Representation
- Implement `__str__` to print rectangle using `#`.
- Empty string if width or height is `0`.
- Implement `__repr__`.

---

### 4. Eval is Magic
- `__repr__` such that `eval(repr(obj))` creates a new instance.

---

### 5. Detect Instance Deletion
- Print `Bye rectangle...` when a `Rectangle` instance is deleted.

---

### 6. How Many Instances
- Class attribute `number_of_instances`:
- Incremented at instantiation, decremented on deletion.

---

### 7. Change Representation
- Class attribute `print_symbol` used for `__str__`, can be any type (default `#`).

---

### 8. Compare Rectangles
- Static method `bigger_or_equal(rect_1, rect_2)` to return the rectangle with the bigger area.
- Raise `TypeError` if arguments are not `Rectangle` instances.

---

### 9. A Square is a Rectangle
- Class method `square(cls, size=0)`: returns a rectangle of width = height = size.

---

## Repository Structure
```
python-more_classes/
├── 0-rectangle.py
├── 1-rectangle.py
├── 2-rectangle.py
├── 3-rectangle.py
├── 4-rectangle.py
├── 5-rectangle.py
├── 6-rectangle.py
├── 7-rectangle.py
├── 8-rectangle.py
├── 9-rectangle.py
└── README.md # 
```

---

## Author

[abo-ah-md](https://github.com/abo-ah-md)
