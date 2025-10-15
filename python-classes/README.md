# Python Classes Project

This directory contains the **Python Classes** project for the Holberton School Higher Level Programming curriculum. The goal of this project is to introduce and reinforce Object-Oriented Programming (OOP) concepts in Python by implementing various tasks and understanding their underlying principles.

---

## Background & Objectives

- **OOP is a cornerstone of modern programming.** In this project, you are strongly encouraged to type (not copy-paste), test, and deeply understand each example and requirement.
- **Key takeaway:** The true value comes from experimenting and practicing OOP yourself – play with it!

---

## Resources

Please complete these in order:

- **Object Oriented Programming:**  
  _Read all content up to (excluding) the "Inheritance" section. Skip class attributes, `classmethod`, and `staticmethod` for now._
- **Object-Oriented Programming:**  
  _Read: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (skip class attributes), Methods, The `__init__` Method, Data Abstraction, Data Encapsulation and Information Hiding, Public/Protected/Private attributes._
- **Properties vs. Getters and Setters**
- **Learn to Program 9: Object Oriented Programming**
- **Python Classes and Objects**
- **Object Oriented Programming**

---

## Learning Objectives

By the end of this project, **you should be able to explain** (without Google):

- What is OOP
- The concept of “first-class everything”
- What is a class
- Difference between a class and an object or instance
- What is an attribute
- How to use public, protected, and private attributes
- The purpose of `self`
- What is a method
- The special `__init__` method
- Concepts of data abstraction, encapsulation, and information hiding
- What is a property, how is it different from an attribute
- How to write Pythonic getters and setters
- How to dynamically create attributes on instances
- How Python binds attributes to objects and classes
- What is the `__dict__` of a class or instance
- How Python finds attributes
- How to use the `getattr` function

---

## Project Requirements

- **Editors:** `vi`, `vim`, or `emacs`
- **Interpreter:** Python 3.8.5 on Ubuntu 20.04 LTS
- **Code Style:** Must follow `pycodestyle` (2.7.*)
- **Scripts:** All your files must be executable and end with a new line
- **Documentation:**  
  - A `README.md` at the project root is **mandatory**
  - Each module, class, and function must contain a proper Google-style docstring, not just single words.  
  - **Example**:
    ```
    """Module docstring: explains the module purpose."""
    
    class Square:
        """Class docstring: describes the Square class."""
        def area(self):
            """Returns the area of the square."""
            pass
    ```
- **Testing:** All file lengths will be tested using `wc`.  
  You may use the sample `main.py` files to test your implementations.

---

## Directory Structure

| File               | Description                                 |
|--------------------|---------------------------------------------|
| `0-square.py`      | Empty class `Square`                        |
| `1-square.py`      | `Square` with private attribute `size`      |
| `2-square.py`      | `Square` with size validation               |
| `3-square.py`      | `Square` with `area()` method               |
| `4-square.py`      | Private `size` with getter and setter       |
| `5-square.py`      | Add `my_print()` method to display square   |
| `6-square.py`      | Add position attribute and validation       |
| `100-singly_linked_list.py` | Implement a singly linked list     |
| `101-square.py`    | Print `Square` instance like `my_print()`   |
| `102-square.py`    | Compare two square instances by area        |
| `README.md`        | **You are here**                            |

---

## Tasks & Progress

All mandatory tasks (0-6) have passed checks for correctness.  
For advanced tasks (7-9), implement them according to the requirements for extra practice and mastery.

---

## Usage

You may test each file with sample scripts such as:

```
#!/usr/bin/python3
Square = import('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.dict)
```
Refer to the project page or each script's comments/examples for further usage details.

---

## Author

Project by [abo-ah-md](https://github.com/abo-ah-md)  
Part of Holberton School Higher Level Programming curriculum.

---
