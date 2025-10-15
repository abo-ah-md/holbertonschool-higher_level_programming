# Python: Everything Is Object

![Python Objects](https://img.icons8.com/color/96/000000/python.png)

## Background

In Python, **everything is an object**. This project explores the behavior and differences between mutable and immutable objects, references, aliasing, and how Python's object model affects assignment, comparisons, and function argument passing.

---

## Key Concepts

### What is an Object?

An **object** in Python is an entity that encapsulates data and behavior. Everything you manipulate—integers, strings, lists, functions—is an object.

### Class vs Object or Instance

- **Class:** A template for creating objects (e.g., `list`, `int`).
- **Object/Instance:** A specific instantiation of a class (e.g., `my_list = [1, 2, 3]`).

### Immutable vs Mutable Object

- **Immutable:** Cannot be changed after creation. (Examples: `int`, `str`, `tuple`)
- **Mutable:** Can be altered after creation. (Examples: `list`, `dict`, `set`)

### Reference, Assignment, and Aliasing

- **Reference:** Links a variable name to an object in memory.
- **Assignment:** Binds a variable to an object (`b = a`).
- **Alias:** Multiple names point to the same object (`m = l`).

### How to Know if Two Variables Are Identical (`is`) vs Equal (`==`)

- `a is b` checks **if both variables refer to the same object** (identity).
- `a == b` checks **if both variables have the same content** (value).

### How to Know if Two Variables Are Linked to the Same Object

Use:
```
print(a is b)
```

### Displaying the Variable Identifier

Use:

```
print(id(a)) # shows the memory address of object 'a'
```

### Built-in Mutable Types

- `list`
- `dict`
- `set`
- `bytearray`

### Built-in Immutable Types

- `int`
- `str`
- `tuple`
- `frozenset`
- `bytes`

### How Python Passes Variables to Functions

Python passes the **reference** to objects. For mutables, changes inside functions affect the caller. For immutables, reassignment inside functions does not affect the caller.

---

## Examples & Insights

### Assignment & Mutation

```
a = 1
b = a
a = 2
print(b) # 1

l =​
m = l
l = 'x'
print(m) # ['x', 2, 3]
```
Changing a mutable object impacts all its aliases. Changing the reference of an immutable doesn't affect other references.

### List Cloning

```
l1 =​
l2 = l1[:] # This creates a copy.
print(l1 is l2) # False
print(l1 == l2) # True
```

### Tuple Nuance
```
a = (1) # Not a tuple, just an integer in parentheses.
a = (1, ) # This is a tuple!
```

### Function Argument Behavior

#### Immutable:
```
def increment(n):
n += 1

a = 1
increment(a)
print(a) # 1
```
#### Mutable:

```
def increment(n):
n.append(4)

l =​
increment(l)
print(l) #​
```

### Special Cases

- List mutation with `+=` (in-place) keeps the identity.
- List reassignment with `+` creates a new object.

---

## Advanced: Memory Details & Efficiency

- Small integers and small strings may be **interned** for efficiency.
- The `LockedClass` example shows how to restrict dynamic attribute creation for memory savings and safety.

---

## Resources

- [Objects and values](https://intranet.hbtn.io/rltoken/vu0q2rKj3XKGyDoqvx72sA)
- [Aliasing](https://intranet.hbtn.io/rltoken/MOP1Saf_C2E_eHxKnZggHw)
- [Immutable vs mutable types](https://intranet.hbtn.io/rltoken/vvV3pDEliqja6aAI7XFNiA)
- [Mutation](https://intranet.hbtn.io/rltoken/Xy3ZTgiwzUL_pLlB2rZoJw)
- [Cloning lists](https://intranet.hbtn.io/rltoken/2tqD3FclxPgvlTC70KQApw)
- [Tuples: immutable but potentially changing](https://intranet.hbtn.io/rltoken/cEGMM3oDORTvSOgUi7Qnhg)
- [Blog post on Dev.to](https://dev.to/aboahmd/understanding-pythons-object-model-mutable-vs-immutable-objects-12m2)

---

## Project Structure

- All answers are in `.txt` files, one line only, no spaces before/after.
- Python scripts use `#!/usr/bin/python3` as the first line.
- Everything follows `pycodestyle` conventions.
- All code is executable and checked by `wc`.

---

## TL;DR

**Truly understanding Python's object model is critical for writing robust, efficient, and predictable code.** Interviews often probe these concepts. Experiment, reason, and study mutation, assignment, and identity—the heart of Python's behavior!
