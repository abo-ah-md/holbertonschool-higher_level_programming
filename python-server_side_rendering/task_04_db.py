from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_products(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return [type('Product', (), prod) for prod in data]

def read_csv_products(filename):
    products = []
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(type('Product', (), product))
            except Exception:
                continue
    return products

def read_sql_products(db_filename, id_filter=None):
    products = []
    error = None
    try:
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        if id_filter is not None:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id=?", (id_filter,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            prod = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products.append(type('Product', (), prod))
        conn.close()
    except Exception as e:
        error = "Database error: " + str(e)
        products = []
    return products, error

@app.route('/products')
def show_products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    error = None
    products = []

    if source == 'json':
        products = read_json_products('products.json')
    elif source == 'csv':
        products = read_csv_products('products.csv')
    elif source == 'sql':
        id_filter = None
        if id_param:
            try:
                id_filter = int(id_param)
            except ValueError:
                error = "Invalid id value"
        products, db_error = read_sql_products('products.db', id_filter)
        if id_param and not error and not products:
            error = "Product not found"
        if db_error:
            error = db_error
    else:
        error = "Wrong source"
    if source in ('json', 'csv') and id_param and not error:
        try:
            id_filter = int(id_param)
            products = [p for p in products if p.id == id_filter]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid id value"
            products = []
    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
