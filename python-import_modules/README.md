# Python Import Modules Project

## Resources

- [Modules](https://intranet.hbtn.io/rltoken/-5iXRN4Q2o9Q6EJtA6IfUQ)
- [Command line arguments](https://intranet.hbtn.io/rltoken/qeCPdm_0U4-RYVqg4vF0dg)
- [Pycodestyle – Style Guide for Python Code](https://intranet.hbtn.io/rltoken/6m4BERWvf2EFhO52UREOvw)
- **Command Line/Manual Help:**  
  - `python3`

## Learning Objectives

By the end of this project, you should be able to explain:

- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments in your Python programs

## Requirements

- **Editors:** vi, vim, emacs
- **OS:** Ubuntu 22.04 LTS
- **Python Version:** 3.10.*
- **Coding Style:** pycodestyle 2.7.*
- **All files must end with a new line**
- **The first line must be:** `#!/usr/bin/python3`
- **A README.md is mandatory**
- **All files must be executable**
- **File length will be tested using `wc`**

## Task List & Completion

| File                        | Task & Description                                                               | Score      |
|-----------------------------|----------------------------------------------------------------------------------|------------|
| `0-add.py`                  | Import `add(a, b)` from `add_0.py` and print `1 + 2 = 3`                        | 100%       |
| `1-calculation.py`          | Import functions from `calculator_1.py`, perform +, -, *, /, print results      | 100%       |
| `2-args.py`                 | Print number and list of arguments passed to the script                          | 100%       |
| `3-infinite_add.py`         | Print sum of all arguments (supports big numbers)                                | 100%       |
| `5-variable_load.py`        | Import variable `a` from `variable_load_5.py` and print its value                | 100%       |
| `4-hidden_discovery.py`     | Print non-__ names from `hidden_4.pyc` (sandbox only)                            | 100%       |
| `100-my_calculator.py`      | Calculator: Import all from `calculator_1.py`, handle usage/errors, operate     | 0%         |
| `101-easy_print.py`         | Print `#pythoniscool` (max 2 lines, no print, eval, open, sys)                   | 0%         |
| `102-magic_calculation.py`  | Implement `magic_calculation(a, b)` exactly as given Python bytecode             | 0%         |
| `103-fast_alphabet.py`      | Print uppercase alphabet, max 3 lines, no loops, conditionals, join, literals    | 0%         |

## Directory Structure

- All source files placed in `python-import_modules/`
- Each file is named according to its task (e.g., `0-add.py`, `1-calculation.py`)
- All files use exact headers and are executable  
- Example main files present for each task

### Example Files

#### `add_0.py`

```
#!/usr/bin/python3
def add(a, b):
"""My addition function
Args:
a: first integer
b: second integer
Returns:
The return value. a + b
"""
return (a + b)
```

#### `calculator_1.py`

```
#!/usr/bin/python3
def add(a, b): return (a + b)
def sub(a, b): return (a - b)
def mul(a, b): return (a * b)
def div(a, b): return int(a / b)
```


## How To Run

1. Make sure all your python files start with `#!/usr/bin/python3`
2. Run with Python 3.10+ on Ubuntu 22.04 LTS:
   - `chmod +x 0-add.py`
   - `./0-add.py`
3. Check style compliance using `pycodestyle`.
4. Use vi/vim/emacs for editing.

## Advanced Tasks (0% Complete)

- `100-my_calculator.py`: Handle imports and argument parsing for basic arithmetic.
- `101-easy_print.py`: Output string without print/eval/open/sys.
- `102-magic_calculation.py`: Reproduce given Python bytecode logic.
- `103-fast_alphabet.py`: Output alphabet without literals or loops.

---

**For detailed requirements, task examples, and source reference, see the individual problem statements in this README.**
