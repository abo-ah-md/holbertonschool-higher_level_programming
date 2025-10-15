# Python Test-Driven Development

Welcome to the **python-test_driven_development** project for Holberton School!  
This repository demonstrates a rigorous approach to Python programming using **Test-Driven Development (TDD)** with a focus on documentation, edge case coverage, and automated testing.

---

## Background & Philosophy

- **Always write documentation and tests _before_ implementation.**
- The intranet checker is not released before the deadline to help students focus on TDD and comprehensive testing.
- Collaboration on test cases is encouraged to ensure coverage of all possible edge cases—but do NOT share actual implementation code.
- Never trust user input blindly; consider ALL possible edge cases in your tests and functions.

---

## Learning Objectives

By working on this repo, you will be able to:

- Explain why Python programming is awesome.
- Understand interactive tests and their value.
- Articulate the importance of thorough testing.
- Write effective Docstrings that double as test cases.
- Document modules and functions with real, meaningful sentences.
- Use basic option flags to run tests.
- Systematically find and handle edge cases.

---

## Requirements

### Python Scripts

- Editors: `vi`, `vim`, `emacs`
- Files must run under Ubuntu 20.04 LTS, Python 3.8.5
- Each file ends with a newline.
- Shebang must be `#!/usr/bin/python3`
- The repo **must** include this `README.md` at root.
- Adhere to `pycodestyle` 2.7.*
- Files must be executable.
- File length checked by `wc`.

### Python Test Cases

- Editors: `vi`, `vim`, `emacs`
- Each test file inside a `tests` folder and ends with a newline.
- Test files have `.txt` extension.
- Run all tests via:  
  `python3 -m doctest ./tests/*`
- All modules/functions must have **real** documentation strings.
- Documentations must explain the purpose in meaningful sentences.
- Collaborate to cover all edge cases in tests—the _checker_ verifies tests first!
- Use `unittest` for Python files with extension `.py` where specified.

---

## Resources

- [doctest — Test interactive Python examples](https://intranet.hbtn.io/rltoken/Hmd_LI8NZ-F2ymDxue5HCg) *(until “26.2.3.7. Warnings” included)*
- [doctest – Testing through documentation](https://intranet.hbtn.io/rltoken/fbFfGNFU07L2yD0D1uc-Xg)
- [Unit Tests in Python](https://intranet.hbtn.io/rltoken/LhbdUZYzqiP7cjxjE3rG3w)

---

## Project Structure

```
python-test_driven_development/
├── 0-add_integer.py
├── 2-matrix_divided.py
├── 3-say_my_name.py
├── 4-print_square.py
├── 5-text_indentation.py
├── 6-max_integer.py
├── tests/
│ ├── 0-add_integer.txt
│ ├── 2-matrix_divided.txt
│ ├── 3-say_my_name.txt
│ ├── 4-print_square.txt
│ ├── 5-text_indentation.txt
│ └── 6-max_integer_test.py
└── README.md
```

---

## Tasks Summary

- **0. Integers addition:**  
  - `add_integer(a, b=98)`  
  - Validates types, casts floats, handles errors, returns integer sum.

- **1. Divide a matrix:**  
  - `matrix_divided(matrix, div)`  
  - Handles matrix type checks, size consistency, division errors, returns a new rounded matrix.

- **2. Say my name:**  
  - `say_my_name(first_name, last_name="")`  
  - Checks string types and prints name format with error handling.

- **3. Print square:**  
  - `print_square(size)`  
  - Prints square of `#`, checks integer type and size constraints.

- **4. Text indentation:**  
  - `text_indentation(text)`  
  - Prints text with 2 new lines after `.`, `?`, `:`, validates string input.

- **5. Max integer - Unittest:**  
  - Added `unittest` tests for `max_integer(list=[])`
  - Ensures `max_integer` works as expected for various cases.

---

## Usage Examples

Run doctests:

```
python3 -m doctest -v ./tests/0-add_integer.txt
```

Run unit tests:
```
python3 -m unittest tests.6-max_integer_test
```

All CLI usage follows Ubuntu 20.04, Python 3.8.5 standards as demonstrated.

---

## Contributing

- Fork and clone the repo.
- Follow TDD: documentation and tests _first_, code _second_.
- Use clean, concise, and compliant code style.
- Collaborate on tests. Share edge case ideas—but keep your own implementation.

---

## Maintainers

- Abdullah Alshebel (a.alshebel.dev@gmail.com)
- [GitHub Profile](https://github.com/abo-ah-md)

---

## License

This project is for educational purposes under Holberton School guidelines.
