# Python OOP – Abstract Classes, Interfaces, Subclassing

Welcome to the **python-abc** directory of the [holbertonschool-higher_level_programming](https://github.com/abo-ah-md/holbertonschool-higher_level_programming) repository. This module is designed to help you master key Object-Oriented Programming (OOP) concepts in Python through structured exercises and practical examples.

---

## Introduction

These exercises will deepen your understanding and practical skill in Python OOP. You will work with:
- **Abstract Classes & Interfaces:** Using Python's `abc` module and enforcing contracts in derived classes.
- **Duck Typing:** Demonstrating Python's flexible type system.
- **Subclassing Standard Base Classes:** Extending built-in types (lists, iterators) for custom behavior.
- **Method Overriding:** Altering or enhancing base class methods.
- **Multiple Inheritance:** Building classes with complex behaviors from multiple sources.
- **Mixins:** Composing behaviors across otherwise unrelated classes.

By completing these tasks, you’ll be proficient in designing, implementing, and testing robust Python programs using advanced OOP principles.

---

## Learning Objectives

- **Abstract Classes:** Define common interfaces and enforce contract completion in subclasses.
- **Interfaces & Duck Typing:** Ensure objects follow required protocols purely by their behavior.
- **Subclassing:** Extend lists, dicts, and iterators for custom structures.
- **Method Overriding:** Change or enhance the logic of inherited methods.
- **Multiple Inheritance:** Combine behaviors from multiple ancestor classes.
- **Mixins:** Modularly add capabilities to multiple classes.

---

## Resources

- [Python 3 Object-Oriented Programming](https://docs.python.org/3/tutorial/classes.html)
- [ABC — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Real Python - OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [Corey Schafer - OOP Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
- [sentdex - Python OOP Tutorial](https://www.youtube.com/playlist?list=PLQVvvaa0QuDdHyKQK4qGbpQzpzSVxrR0b)

Both reading, code, and video resources are provided to suit different learning styles.

---

## Task Overview

### 0. Abstract Animal Class and its Subclasses
**Goal:**  
Create an abstract `Animal` class with an abstract method `sound`.  
Implement `Dog` and `Cat` subclasses with their own `sound` methods.

**Key Concepts:**  
- Use `abc.ABC` and `@abstractmethod` to enforce subclass implementation.

**Sample Output:**
```
Bark
Meow
TypeError: Can't instantiate abstract class Animal with abstract method sound
```

---

### 1. Shapes, Interfaces, and Duck Typing
**Goal:**  
Create an abstract `Shape` class with `area` and `perimeter` methods.  
Implement `Circle` and `Rectangle` classes and a function `shape_info` that prints info (using duck typing).

**Key Concepts:**  
- Duck typing: Do not check types, trust methods' existence.
- Abstract base class enforces method contracts.

**Sample Output:**
```
Area: 78.5398...
Perimeter: 31.4159...
Area: 28
Perimeter: 22
```
---

### 2. Extending the Python List with Notifications
**Goal:**  
Build a `VerboseList` class extending Python’s list.  
Override `append`, `extend`, `remove`, and `pop` to print notifications on list modification.

**Key Concepts:**  
- Subclassing built-in types.
- Method overriding with `super()`.

**Sample Output:**

```
Added to the list.
Extended the list with items.
Removed from the list.
Popped from the list.
Popped from the list.​
```

---

### 3. CountedIterator – Keeping Track of Iteration
**Goal:**  
Implement `CountedIterator` that extends Python’s iterator.  
Keep count of the number of iterated items.

**Key Concepts:**  
- Subclassing iterator protocol.
- Overriding `__next__`.

**Sample Output:**
```
Got 1, total 1 items iterated.
Got 2, total 2 items iterated.
...
No more items.
```

---

### 4. The Enigmatic FlyingFish – Multiple Inheritance
**Goal:**  
Create a `Fish` class (`swim`, `habitat`) and a `Bird` class (`fly`, `habitat`).
Implement `FlyingFish` inheriting both; override certain behaviors.

**Key Concepts:**  
- Multiple inheritance.
- Method Resolution Order (MRO).

**Sample Output:**

```
The flying fish is swimming!
The flying fish is soaring!
The flying fish lives both in water and the sky!
```

---

### 5. The Mystical Dragon – Mastering Mixins
**Goal:**  
Design `SwimMixin` and `FlyMixin` classes.  
Create a `Dragon` class utilizing both for swimming and flying abilities; optionally add a `roar` method.

**Key Concepts:**  
- Mixins: Lightweight, single-feature behaviors.
- Composability.

**Sample Output:**
```
The creature swims!
The creature flies!
The dragon roars!
```

---

## Directory and File Structure
```
python-abc/
│
├── README.md # This readme
├── main.py # Optional main runner file
├── task_00_abc.py # Abstract class example
├── task_01_duck_typing.py
├── task_02_verboselist.py
├── task_03_countediterator.py
├── task_04_flyingfish.py
├── task_05_dragon.py
```

---

## Usage

Each task has its corresponding test script (main\_XX\_*.py - see above in each section).  
Clone the repo and run each as needed using Python 3.

```
python3 main_00_abc.py
python3 main_01_duck_typing.py
```

---

## Contributing

Pull requests and suggestions welcome! Please follow standard Python style guidelines and clear commit messages.

---

## License

See LICENSE file in the parent repo.

---

Happy coding with Python OOP!
