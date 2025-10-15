# Python Exceptions Project

## 📚 Resources
- Errors and Exceptions [[intranet link]](https://intranet.hbtn.io/rltoken/WxV68L6c_WRMEzZt8P7oIA)
- Learn to Program 11: Static & Exception Handling [[intranet link, start at minute 7]](https://intranet.hbtn.io/rltoken/OTYmJ8UpJotqIVyrVgSL4A)

## 🎯 Learning Objectives

By completing this project, you will be able to explain:
- **Why Python programming is awesome**
- **The difference between errors and exceptions**
- **What exceptions are and how to use them**
- **When and why to use exceptions**
- **How to correctly handle exceptions**
- **The purpose of catching exceptions**
- **How to raise built-in exceptions**
- **When to implement a clean-up action after an exception**

## 📝 Requirements

- **Allowed editors:** `vi`, `vim`, `emacs`
- **OS:** Ubuntu 20.04 LTS, Python 3.8.5
- **File formatting:**
  - All files must end with a new line.
  - The first line of every file: `#!/usr/bin/python3`
  - All code must pass `pycodestyle` (version 2.7.*).
  - Every file must be executable.
  - File length tested using `wc`.
- A README.md file at the root of the project is **mandatory**.

## 🚀 Tasks Overview

### 0. Safe List Printing
- **File:** `0-safe_print_list.py`
- Print `x` elements from a list, any type.
- Use `try:/except:`, **no imports**, **no len()**.
- Returns number of elements printed.

### 1. Safe Printing of an Integers List
- **File:** `1-safe_print_integer.py`
- Print integer using `"{:d}".format()`.
- Returns `True` if printed as integer, else `False`.
- Use `try:/except:`, **no type() check, no imports**.

### 2. Print and Count Integers
- **File:** `2-safe_print_list_integers.py`
- Prints first `x` elements from a list, only integers.
- Skips non-integer values silently.
- Returns count of integers printed.
- Use `try:/except:`, **no imports**, **no len()**.

### 3. Integers Division with Debug
- **File:** `3-safe_print_division.py`
- Divides two integers, prints result in `finally:` section with "Inside result: ".
- Returns result or `None`.
- Use `try:/except:/finally:`, **no imports**.

### 4. Divide a List
- **File:** `4-list_division.py`
- Divides element-wise two lists, with length support.
- Returns a list with results.
- If division fails: returns `0`, prints error messages as instructed.
- Use `try:/except:/finally:`, **no imports**.

### 5. Raise Exception
- **File:** `5-raise_exception.py`
- Raises a type exception.
- **No imports**.

### 6. Raise a Message
- **File:** `6-raise_exception_msg.py`
- Raises a name exception with a custom message.
- **No imports**.

## 🗂 Repository Structure

```
python-exceptions/
│
├── 0-safe_print_list.py
├── 1-safe_print_integer.py
├── 2-safe_print_list_integers.py
├── 3-safe_print_division.py
├── 4-list_division.py
├── 5-raise_exception.py
├── 6-raise_exception_msg.py
└── README.md
```

## 💡 Usage Example

### Example for Task 0

```
#!/usr/bin/python3
safe_print_list = import('0-safe_print_list').safe_print_list

my_list =​
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
```

## ✅ Test Results

- All tasks completed and tested successfully (`100%` scores).

---

**For any questions, refer to the intranet resources or check the provided code examples.**

