# Python More Data Structures

## Overview

This project explores advanced usage of Python data structures, including sets and dictionaries, as well as key functional programming tools: lambda functions, `map`, `reduce`, and `filter`. Each task is designed to deepen understanding of these concepts with practical, hands-on coding.

---

## Resources

- [Data structures](https://intranet.hbtn.io/rltoken/K8JSw_eMWjw6EzmAL1S8bQ)
- [Lambda, filter, reduce and map](https://intranet.hbtn.io/rltoken/JMc02-iMawLlxGCsnEalXA)
- [Learn to Program 12 Lambda Map Filter Reduce](https://intranet.hbtn.io/rltoken/NnWm29rFmdDcjcdRQX1tEw)

---

## Learning Objectives

By completing this project, you will be able to explain:

- **Why Python programming is awesome**
- **What sets are and how to use them**
- **Common set methods and their usage**
- **When to use sets versus lists**
- **How to iterate into a set**
- **What dictionaries are, and dictionary basics**
- **When to use dictionaries versus lists/sets**
- **What is a key in a dictionary**
- **How to iterate over a dictionary**
- **What is a lambda function**
- **What are the `map`, `reduce`, and `filter` functions**

---

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- Each file ends with a new line and starts with: `#!/usr/bin/python3`
- A `README.md` at the project root is **mandatory**
- Code must follow `pycodestyle` (version 2.7.*)
- All files must be executable
- File lengths will be checked using `wc`

---

## Task List

| # | Task | Description |
|---|------|-------------|
| 0 | Squared simple | Compute square values of a matrix. Prototype: `def square_matrix_simple(matrix=[])` |
| 1 | Search and replace | Replace occurrences of an element in a new list. Prototype: `def search_replace(my_list, search, replace)` |
| 2 | Unique addition | Add all unique integers in a list. Prototype: `def uniq_add(my_list=[])` |
| 3 | Present in both | Return common elements in two sets. Prototype: `def common_elements(set_1, set_2)` |
| 4 | Only differents | Return all elements present in only one set. Prototype: `def only_diff_elements(set_1, set_2)` |
| 5 | Number of keys | Return number of keys in a dictionary. Prototype: `def number_keys(a_dictionary)` |
| 6 | Print sorted dictionary | Print dictionary by ordered keys. Prototype: `def print_sorted_dictionary(a_dictionary)` |
| 7 | Update dictionary | Replace or add key/value in a dictionary. Prototype: `def update_dictionary(a_dictionary, key, value)` |
| 8 | Simple delete by key | Delete a key in a dictionary. Prototype: `def simple_delete(a_dictionary, key="")` |
| 9 | Multiply by 2 | Return new dictionary with all values multiplied by 2. Prototype: `def multiply_by_2(a_dictionary)` |
| 10 | Best score | Return a key with the biggest integer value. Prototype: `def best_score(a_dictionary)` |
| 11 | Multiply by using map | Return a list with all values multiplied by a number using map. Prototype: `def multiply_list_map(my_list=[], number=0)` |
| 12 | Roman to Integer | Convert a Roman numeral to an integer. Prototype: `def roman_to_int(roman_string)` |

---

## Example Usage

Below are sample usages for some of the major tasks:

### Squared Simple

```
matrix = ,​
,

]
new_matrix = square_matrix_simple(matrix)
print(new_matrix) # , , ]​
print(matrix) # , , ]​
```

### Search and Replace

```
my_list =​
new_list = search_replace(my_list, 2, 89)
print(new_list) #​
print(my_list) #​
```

### Roman to Integer

```
print("X =", roman_to_int("X")) # X = 10
print("VII =", roman_to_int("VII")) # VII = 7
print("IX =", roman_to_int("IX")) # IX = 9
print("LXXXVII =", roman_to_int("LXXXVII")) # LXXXVII = 87
print("DCCVII =", roman_to_int("DCCVII")) # DCCVII = 707
```

---

## File Structure

- `0-square_matrix_simple.py`
- `1-search_replace.py`
- `2-uniq_add.py`
- `3-common_elements.py`
- `4-only_diff_elements.py`
- `5-number_keys.py`
- `6-print_sorted_dictionary.py`
- `7-update_dictionary.py`
- `8-simple_delete.py`
- `9-multiply_by_2.py`
- `10-best_score.py`
- `11-multiply_list_map.py`
- `12-roman_to_int.py`
- `README.md`

---

## Notes

- Each task is **fully tested** and follows project guidelines for code style and structure.
- Refer to sample usage for expected input and output behaviors.
- For interview preparation (Task 12), ensure Roman numeral conversions are handled as described.

---

**Explore the source files to learn and implement each function. Happy coding!**
