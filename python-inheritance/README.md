# Python Inheritance Project

## 📚 Resources
Read or watch:
- [Inheritance](https://intranet.hbtn.io/rltoken/pRigaMtzlZIXHVXZJ7yRMQ)
- [Multiple inheritance](https://intranet.hbtn.io/rltoken/q7hgZ43Gu_snerCNUwqzuw)
- [Inheritance in Python](https://intranet.hbtn.io/rltoken/04VYC46DWxWLhcUpRVmHGg)
- [Learn to Program 10: Inheritance Magic Methods](https://intranet.hbtn.io/rltoken/fojEQ8bllfZecx-ZKKurTw)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to **explain** the following concepts in Python inheritance:

- What is a **superclass, baseclass, or parentclass**
- What is a **subclass**
- How to **list all attributes and methods** of a class or instance
- **When** can an instance have new attributes
- How to **inherit a class from another**
- How to **define a class with multiple base classes**
- What is the **default class** every class inherits from
- How to **override** a method or attribute inherited from the base class
- Which attributes or methods are available **by heritage** to subclasses
- **Purpose** of inheritance
- What are, when, and how to use **isinstance**, **issubclass**, **type**, and **super** built-in functions

---

## 🗂️ Requirements

- All scripts **must be Python3 (3.8.5)** and run on **Ubuntu 20.04 LTS**
- Allowed editors: `vi`, `vim`, `emacs`
- All files should **end with a new line**
- The first line of all your scripts *must be* `#!/usr/bin/python3`
- **README.md** at the root of the project folder is mandatory
- Code must follow **pycodestyle** (version 2.7.\*)
- All files **must be executable**
- File lengths will be tested using `wc`

#### Python Test Cases
- All test files should be in a folder named `tests`
- Test files must have `.txt` extension
- Tests should be executed using: `python3 -m doctest ./tests/*`

#### Documentation
- Every **module**, **class**, and **function** must have a meaningful documentation string explaining its purpose (length will be checked).
- Do **not** use the words `import` or `from` inside comments (the checker flags attempts to import).

#### Collaboration
- Work together on test cases to ensure coverage of edge cases.

---

## 📒 Task Overview

### 0. Lookup
- Write a function `lookup(obj)` to return a list of available attributes and methods of an object, **without importing any module**.

### 1. MyList
- Create a class `MyList` inheriting from `list`.
- Implement `print_sorted(self)` to print the list sorted in ascending order.

### 2. Exact same object
- Function `is_same_class(obj, a_class)` returns True if the object is **exactly** of the specified class, otherwise False.

### 3. Same class or inherit from
- Function `is_kind_of_class(obj, a_class)` returns True if the object is an instance of, or inherits from, the specified class.

### 4. Only subclass of
- Function `inherits_from(obj, a_class)` returns True if the object is an instance of a class that **inherited** from the specified class.

### 5. Geometry module
- Create an **empty class** `BaseGeometry`.

### 6. Improve Geometry
- Update `BaseGeometry` to include `area(self)`, which raises an Exception (`area() is not implemented`).

### 7. Integer validator
- Extend `BaseGeometry` with `integer_validator(self, name, value)` to validate that value is a positive integer.

### 8. Rectangle
- Implement `Rectangle` inheriting from `BaseGeometry`, with private `width` and `height` validated as positive integers.

### 9. Full rectangle
- In `Rectangle`, implement `area()` and `__str__`/`__repr__` for `[Rectangle] <width>/<height>` representation.

### 10. Square #1
- Implement `Square` inheriting from `Rectangle`, with private `size` validated.

### 11. Square #2
- In `Square`, implement `area()` and print/str as `[Square] <width>/<height>`.

---

## 📂 File Structure

```
python-inheritance/
├── 0-lookup.py
├── 1-my_list.py
├── 2-is_same_class.py
├── 3-is_kind_of_class.py
├── 4-inherits_from.py
├── 5-base_geometry.py
├── 6-base_geometry.py
├── 7-base_geometry.py
├── 8-rectangle.py
├── 9-rectangle.py
├── 10-square.py
├── 11-square.py
├── main.py
├── tests/
│ ├── 1-my_list.txt
│ ├── 7-base_geometry.txt
└── README.md
```

---

## 💡 Usage and Examples

See each task script for demonstration and expected output.  
Tests provided illustrate correct usage and edge cases.

---

## 📝 Best Practices

- Follow PEP-8 with pycodestyle 2.7.\*
- Use clear, meaningful docstrings.
- Don’t use `import` or `from` in comments.
- Collaborate on test cases for broad coverage.

---

## 🚩 Repository

GitHub: [holbertonschool-higher_level_programming](https://github.com/abo-ah-md/holbertonschool-higher_level_programming)  
Project Directory: `python-inheritance`
