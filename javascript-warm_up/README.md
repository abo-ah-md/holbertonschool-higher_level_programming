# JavaScript Warm Up

This repository contains introductory scripts and mini-projects for learning basic JavaScript concepts, scripting, and web front-end. The tasks here equip you with essential skills for using JavaScript in automation (like Python scripting) and dynamic website development (to later power projects such as AirBnB clone with JavaScript and JQuery).

## Background

JavaScript is a versatile, widely-used programming language that enables scripting for automation and dynamic web front-ends.

In this project, you'll:
- Practice scripting with Node.js
- Master the basics before moving to dynamic web tasks with JavaScript & JQuery

---

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)

---

## Resources

Recommended readings & tutorials:

- [Writing JavaScript Code](https://intranet.hbtn.io/rltoken/fQUkQNjfE1Dw47vcgps6Ig)
- [Variables](https://intranet.hbtn.io/rltoken/FX6qEtLyELhXUg7u23eMDg)
- [Data Types](https://intranet.hbtn.io/rltoken/R5-aJ7W7ypXbTAcI54Ut-g)
- [Operators](https://intranet.hbtn.io/rltoken/fQUkQNjfE1Dw47vcgps6Ig)
- [Operator Precedence](https://intranet.hbtn.io/rltoken/4PdyDQJJuDXEZmbALqttug)
- [Controlling Program Flow](https://intranet.hbtn.io/rltoken/N0Np7QFZVwSnRopkHsN4ow)
- [Functions](https://intranet.hbtn.io/rltoken/21XrxDV4cjQfW8v7r2FNMw)
- [Objects and Arrays](https://intranet.hbtn.io/rltoken/LSNtL9tP1DBU0bnBLdF2uA)
- [Module patterns](https://intranet.hbtn.io/rltoken/OOAH-N9qs-oT4Y32ErUELQ)
- [var, let and const](https://intranet.hbtn.io/rltoken/5dIWvs6Zn5XjcsP18Ti9Uw)
- [JavaScript Tutorial](https://intranet.hbtn.io/rltoken/PzZBOx5Ms7RL0FX1fihHKw)
- [Modern JS](https://intranet.hbtn.io/rltoken/toueHB-cJAYoXNscJtr3Jw)

---

## Learning Objectives

On completing this project, you will be able to explain:

- Why JavaScript programming is amazing
- How to run a JavaScript script
- How to create variables and constants, and differences between `var`, `const`, and `let`
- All available data types in JavaScript
- Using `if`, `if ... else` statements, and comments
- Assigning values to variables
- Using `while` and `for` loops; using `break` and `continue`
- Functions and their usage
- What a function returns when there's no `return` statement
- Variable scope
- Arithmetic operators and their usage
- Manipulating dictionaries (objects)
- Importing a file in Node.js

---

## Requirements

- **Allowed editors:** vi, vim, emacs
- **Interpreter:** Ubuntu 20.04 LTS, Node.js v14.x
- **Shebang:** All files start with `#!/usr/bin/node`
- **README:** This README.md must exist at the root
- **Code style:** Semistandard (v16.x.x), AirBnB style. Install with:
```
sudo npm install semistandard --global
```
- **Executability:** All files should run via `node <file>`
- **File length:** Checked by `wc`
- **All outputs printed with `console.log(...)`**
- **No usage of `var`**

---

## Setup Instructions

**Node.js 14 Installation**
```
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

**Semistandard Installation**

```
sudo npm install semistandard --global
```

---

## Tasks

Each numbered file matches a task. Below are key highlights:

### 0. First constant, first print
Prints “JavaScript is amazing”  
- File: `0-javascript_is_amazing.js`

### 1. 3 languages
Prints three lines:  
- “C is fun”  
- “Python is cool”  
- “JavaScript is amazing”  
- File: `1-multi_languages.js`

### 2. Arguments
Responds depending on argument count:
- “No argument”, “Argument found”, “Arguments found”
- File: `2-arguments.js`

### 3. Value of my argument
Prints the first argument or “No argument”
- File: `3-value_argument.js`

### 4. Create a sentence
Prints two arguments in the format: `<arg1> is <arg2>`
- File: `4-concat.js`

### 5. An Integer
Prints “My number: <integer>” or “Not a number”
- File: `5-to_integer.js`

### 6. Loop to languages
Prints three strings from an array in a loop, with only one `console.log`
- File: `6-multi_languages_loop.js`

### 7. I love C
Prints “C is fun” x times, where x is an integer argument
- File: `7-multi_c.js`

### 8. Square
Prints a square of “X” based on integer argument; handles errors
- File: `8-square.js`

### 9. Add
Prints the sum of two arguments using a defined `add(a, b)` function
- File: `9-add.js`

### 10. Factorial
Prints factorial of argument, recursively
- File: `10-factorial.js`

### 11. Second biggest!
Prints the second largest integer among arguments or 0 if not enough arguments
- File: `11-second_biggest.js`

### 12. Object
Updates an object's value from 12 to 89
- File: `12-object.js`

### 13. Add file
Exports a function `add` for integer addition
- File: `13-add.js`

### Advanced Tasks

#### 14. Const or not const
Modifies `myVar` to 333  
- File: `100-let_me_const.js`

#### 15. Call me Moby
Executes a function x times (`callMeMoby(x, theFunction)`)
- File: `101-call_me_moby.js`

#### 16. Add me maybe
Increments and calls a function (`addMeMaybe(number, theFunction)`)
- File: `102-add_me_maybe.js`

#### 17. Increment object
Adds function `incr` to object to increment its value
- File: `103-object_fct.js`

---

## Project Structure

```
javascript-warm_up/
├── .gitignore
├── 0-javascript_is_amazing.js
├── 1-multi_languages.js
├── 2-arguments.js
├── 3-value_argument.js
├── 4-concat.js
├── 5-to_integer.js
├── 6-multi_languages_loop.js
├── 7-multi_c.js
├── 8-square.js
├── 9-add.js
├── 10-factorial.js
├── 11-second_biggest.js
├── 12-object.js
├── 13-add.js
├── 100-let_me_const.js
├── 101-call_me_moby.js
├── 102-add_me_maybe.js
├── 103-object_fct.js
├── README.md
├── package.json
└── package-lock.json
```

---

## Tips

- Use only allowed syntax (`const`/`let`, no `var`)
- Follow semistandard and AirBnB style rules
- Run scripts with `node <script.js>`
- Check documentation and resources for patterns and advanced features

Happy coding!
