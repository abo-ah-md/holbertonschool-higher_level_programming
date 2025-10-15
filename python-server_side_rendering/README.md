# Python Server-Side Rendering Project

A guided Python/Flask project for implementing **server-side rendering (SSR)** using the Jinja templating engine, featuring dynamic data display from JSON, CSV, and SQLite sources. The project demonstrates how to build scalable, efficient, and SEO-friendly web applications, emphasizing template reuse, error handling, and dynamic content.

---

## 🌟 Overview

**Server-side rendering** generates full HTML pages on the server, sending them directly to the client. Unlike client-side rendering—where the browser builds the web page using JavaScript—SSR boosts SEO, improves load efficiency, and provides dynamic, maintainable solutions for web apps.

**In this project, you will:**
- Understand SSR concepts and compare with client-side rendering.
- Learn benefits of SSR in modern web development.
- Build SSR web pages using Python, Flask, and Jinja.
- Display data from JSON, CSV, and SQLite.
- Handle dynamic content and user inputs in pages.

---

## 🚀 Learning Objectives

- **Grasp SSR vs CSR:** Comprehend how server-side and client-side rendering differ.
- **SSR Benefits:** Know why SSR boosts SEO, efficiency, and maintainability.
- **Python Implementation:** Implement SSR using Flask and Jinja.
- **Template Mastery:** Use Jinja to generate dynamic HTML pages.
- **Multi-source Data:** Read/display data from JSON, CSV, and SQLite.
- **Dynamic UI:** Handle dynamic user content in Flask web applications.

---

## 📁 Repo Structure
```
python-server_side_rendering/
│
├── templates/ # HTML/Jinja templates (index, header, footer, about, contact, items, products)
├── create_products_db.py # Script to create and seed SQLite database
├── items.json # Sample items for dynamic template
├── products.csv # Products sample data in CSV format
├── products.json # Products sample data in JSON format
├── task_00_intro.py # Invitation file generator with error handling
├── task_01_jinja.py # Basic Flask app with reusable header/footer
├── task_02_logic.py # Flask dynamic template with loops/conditions
├── task_03_files.py # Display data from JSON/CSV via Flask route
├── task_04_db.py # Display data from SQLite alongside JSON/CSV
```

---

## 📝 Tasks & Features

### **0. Simple Templating Program**
Generate personalized invitation files from a single template and attendee objects.
- Template placeholders: `{name}`, `{event_title}`, `{event_date}`, `{event_location}`
- Edge-case handling: empty template, empty list, missing object data, invalid input types
- Output files: `output_X.txt` for each attendee

### **1. Basic HTML Template in Flask**
Create Flask app with reusable header/footer.
- Main HTML file: `index.html` (heading, paragraph, list)
- Header/footer included via Jinja `{% include %}`
- Additional pages: `about.html`, `contact.html`
- Flask routes: `/`, `/about`, `/contact`

### **2. Dynamic Template with Loops & Conditions**
Render items from a JSON file using Jinja loops/conditions.
- Data: `items.json` → `{ "items": [...] }`
- Template: displays list or "No items found"
- Route `/items` displays items

### **3. Display Data from JSON or CSV**
Show products table from either JSON or CSV, filterable by `id`.
- Data: `products.json`, `products.csv`
- Route `/products?source=json|csv&id=<id>`
- Error handling: wrong source/id not found
- Unified template: `product_display.html`

### **4. Add SQLite Database Support**
Extend data display to support SQLite.
- Data source: `products.db` (Products table with id, name, category, price)
- Route `/products?source=sql&id=<id>`
- Script: `create_products_db.py` creates and seeds DB
- Template: same as for JSON/CSV
- Edge-case handling for DB errors

---

## 🔗 Resources and Documentation

- [MDN Server-Side Web Development](https://intranet.hbtn.io/rltoken/I1-8Brx2B5Vcq1DL8xfP1A)
- [Templating Engines in Web Development](https://intranet.hbtn.io/rltoken/FErUnxmyagdWQmd1od8Yhg)
- [Flask Official Documentation](https://intranet.hbtn.io/rltoken/2xcmHzNd4lk9WkFqCy5Mlw)
- [Python JSON Documentation](https://intranet.hbtn.io/rltoken/lC6m9GFhAWqgqvmSlA3y5g)
- [Python CSV Documentation](https://intranet.hbtn.io/rltoken/FwAYKq-BrdtZlNodGDxsag)
- [Python SQLite Documentation](https://intranet.hbtn.io/rltoken/wPc6yZmq5N00DfY5cfWRYQ)
- [Jinja2 Documentation](https://intranet.hbtn.io/rltoken/Hz3FkY15qDQWE31oBwe-eA)

---

## 💡 Usage & Running

1. **Install dependencies**  
   Run: `pip install Flask`

2. **Run any Flask task file**  
   Example:  
   `python task_01_jinja.py`

3. **Create and seed database**  
   Run:  
   `python create_products_db.py`

4. **Access web app via browser**  
   - Homepage: `http://localhost:5000/`
   - Products: `http://localhost:5000/products?source=json`
   - Items: `http://localhost:5000/items`

---

## 📚 Example Data

**Sample attendees:**  
```
attendees = [
{"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
{"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
{"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]
```

**Sample products (JSON):**  
```
[
{"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
{"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
]
```

---

## 🛠️ Hints & Best Practices

- Use Jinja `{% include 'header.html' %}` for reusable components.
- Always validate input types and handle edge cases with meaningful error messages.
- Experiment with empty/invalid JSON, CSV, and DB sources to check error handling.
- Test all available routes in your Flask app to ensure full dynamic functionality.
- For database setup, run `create_products_db.py` before querying with source=sql.

---

## 👨‍💻 Authors

Project maintained by [abo-ah-md](https://github.com/abo-ah-md) for **holbertonschool-higher_level_programming**.

---

## 📄 License

This project is for educational use and may be forked under [MIT License](https://opensource.org/licenses/MIT).

