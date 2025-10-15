# JavaScript DOM Manipulation

Welcome to the **JavaScript DOM Manipulation** project in the `holbertonschool-higher_level_programming` repository. This project explores and implements key concepts of JavaScript for interacting with the Document Object Model (DOM) in dynamic web pages.

---

## 📚 Resources

To master JavaScript DOM manipulation, read or watch the following foundational resources:

- [What is JavaScript?](https://intranet.hbtn.io/rltoken/BRGugPVlpApb5CMpWDZZyw)
- [Introduction to the DOM](https://intranet.hbtn.io/rltoken/_IqetddeDl77jcNAfU8lSQ)
- [Document Interface](https://intranet.hbtn.io/rltoken/VBwvMfwoElIcvVa-Rc9LJg)
- [Element Class](https://intranet.hbtn.io/rltoken/3f2toV3UxRn01mxEV3o9Xg)
- [Locating DOM elements using selectors](https://intranet.hbtn.io/rltoken/NyjqeBe3dWe3zov5KTcylw)
- [CSS Selectors](https://intranet.hbtn.io/rltoken/gkU6EEJQHeh4-TFAq9vgAg)
- [CSS Diner](https://intranet.hbtn.io/rltoken/GunCAsRgUiuvrDkp07w6jw) (Practice with selectors)
- [DOM Scripting](https://intranet.hbtn.io/rltoken/IyYBDmVhUL-DAbLlMkeJWQ)
- [Network Requests](https://intranet.hbtn.io/rltoken/sqJbOOIcK_OQGQGW6VXhKw)
- [What went wrong? Troubleshooting JavaScript](https://intranet.hbtn.io/rltoken/vudThPsuSBng13jFlPyI0Q)

---

## 🎯 Learning Objectives

After completing this project, you should be able to:

- **Select HTML elements in JavaScript**
- Understand **ID, class, and tag name** selectors
- **Modify element styles** and classes
- **Get and update content** of HTML elements
- **Manipulate the DOM** dynamically
- Make network requests using **XMLHttpRequest** and the **Fetch API**
- **Listen/bind to DOM and user events**

---

## 📝 Requirements

- **Allowed editors:** All
- **Interpreter:** Chrome browser version 57.0 or later
- **File endings:** All files must end with a new line
- Create a **meaningful README.md** in this directory
- Use **semistandard** compliant code
- **Do NOT use** `var`
- The HTML page **should not reload** for DOM updates or data fetches

---

## 🚀 Directory Structure

All scripts for the tasks are in this directory:

- `0-script.js` through `8-script.js` (basic tasks)
- `100-script.js`, `101-script.js` (advanced tasks)
- Example HTML files for testing tasks (`main.html`, `0-main.html`, ...)
- **[README.md](README.md)** – You are reading it!

---

## 🗂️ Tasks & Descriptions

Each numbered script file addresses a specific DOM manipulation scenario. **Test** with the provided HTML examples.

### 0. Color Me
Update header text color to **red** using `document.querySelector`.

### 1. Click and turn red
Update header color to **red** when clicking element with id `red_header`.

### 2. Add `.red` class
Add the class `red` to the header when clicking element with id `red_header`.

### 3. Toggle classes
Toggle header's class between `red` and `green` on `toggle_header` click.

### 4. List of elements
Add new `<li>Item</li>` to list `.my_list` on `add_item` click.

### 5. Change the text
Change header text to **"New Header!!!"** on `update_header` click.

### 6. Star Wars character
Fetch and display character name from [SWAPI](https://swapi-api.hbtn.io/api/people/5/?format=json) in `character` element.

### 7. Star Wars movies
Fetch and list all Star Wars movie titles from [SWAPI Films](https://swapi-api.hbtn.io/api/films/?format=json) in `list_movies`.

### 8. Say Hello!
Fetch and display "hello" in French using [HelloSalut API](https://hellosalut.stefanbohacek.com/?lang=fr) in `hello` element.

---

#### 🔥 Advanced Tasks

### 9. List, add, remove
Add, remove, or clear `<li>Item</li>` elements in `my_list` using `add_item`, `remove_item`, and `clear_list` controls.

### 10. Say hello to everybody!
Fetch translation of "Hello" for selected language code using HelloSalut API, triggered by `btn_translate`.

---

## 🧑‍💻 Usage Instructions

- Place the script files in the appropriate directory
- Use the provided HTML files for live testing in Chrome (57+)
- Ensure all DOM changes are dynamic, **without page reloads**
- Maintain **code quality** and **semistandard** style

---

## 📦 Project Files

- Each task is implemented in its respective JS script:  
  `0-script.js`, `1-script.js`, ..., `8-script.js`, `100-script.js`, `101-script.js`
- Example HTML files are provided for each feature
- For details see [GitHub directory listing](https://github.com/abo-ah-md/holbertonschool-higher_level_programming/tree/main/javascript-dom_manipulation)

---

## 🤝 Credits

This project follows the [Holberton School](https://www.holbertonschool.com/) methodology and was built as part of higher-level programming curriculum requirements.  
Developed by [abo-ah-md](https://github.com/abo-ah-md).

---

## 🛠️ Support & Contribution

Found a bug, or want to contribute?  
- Fork the repository
- Create a pull request
- Open issues for improvements or questions

---

**Happy DOM Manipulating!**
