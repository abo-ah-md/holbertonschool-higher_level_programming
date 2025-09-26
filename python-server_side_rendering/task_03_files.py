from flask import Flask, render_template, request
import json
import csv

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
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error, products=[])

    
    if id_param:
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
