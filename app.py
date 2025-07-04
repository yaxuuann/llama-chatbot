from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

HUGGINGFACE_API_KEY = "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"
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-3B-Instruct"

def load_products_from_csv():
    csv_path = os.path.join(app.static_folder, 'data', 'df_sale_cleaned.csv')
    products_df = pd.read_csv(csv_path)

    # Drop duplicates based on product_id
    products_df = products_df.drop_duplicates(subset=['product_id'])

    # Transform the data to match the expected structure
    products = products_df.to_dict('records')

    # Add any additional missing fields with default values
    for product in products:
        product['category'] = product['product_type']  # Use product_type as category

    return products

products = load_products_from_csv()

@app.route('/products')
def product_listing():
    category = request.args.get('category', 'all')
    filtered_products = products
    if category != 'all':
        filtered_products = [p for p in products if p['category'].upper() == category.upper()]

    return render_template('productlisting.html', products=filtered_products, selected_category=category)


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    prompt = data.get('prompt')

    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch response from the API."}), response.status_code


@app.route('/product/<product_id>')
def product_details(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return redirect(url_for('product_listing'))
    return render_template('productdetails.html', product=product, products=products)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    cart_products = []
    total = 0

    for item in cart_items:
        product = next((p for p in products if str(p['id']) == str(item['product_id'])), None)
        if product:
            cart_product = product.copy()
            cart_product['quantity'] = item['quantity']
            cart_product['subtotal'] = product['price'] * item['quantity']
            cart_products.append(cart_product)
            total += cart_product['subtotal']

    return render_template('cart.html', cart_products=cart_products, total=total)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity', 1)

    if 'cart' not in session:
        session['cart'] = []

    product = next((p for p in products if str(p['id']) == str(product_id)), None)
    if not product:
        return jsonify({'success': False, 'message': 'Product not found'})

    if product['stock'] < quantity:
        return jsonify({'success': False, 'message': 'Insufficient stock'})

    cart = session['cart']
    existing_item = next((item for item in cart if str(item['product_id']) == str(product_id)), None)

    if existing_item:
        new_quantity = existing_item['quantity'] + quantity
        if new_quantity > product['stock']:
            return jsonify({'success': False, 'message': 'Insufficient stock'})
        existing_item['quantity'] = new_quantity
    else:
        cart.append({'product_id': product_id, 'quantity': quantity})

    session['cart'] = cart
    session.modified = True

    return jsonify({'success': True, 'message': 'Product added to cart'})

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    product_id = request.json.get('product_id')

    if 'cart' in session:
        session['cart'] = [item for item in session['cart'] if str(item['product_id']) != str(product_id)]
        session.modified = True

    return jsonify({'success': True, 'message': 'Product removed from cart'})

@app.route('/update_cart', methods=['POST'])
def update_cart():
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity', 1)

    if 'cart' in session:
        for item in session['cart']:
            if str(item['product_id']) == str(product_id):
                product = next((p for p in products if str(p['id']) == str(product_id)), None)
                if product and quantity <= product['stock']:
                    item['quantity'] = quantity
                    session.modified = True
                    return jsonify({'success': True, 'message': 'Cart updated'})
                else:
                    return jsonify({'success': False, 'message': 'Insufficient stock'})

    return jsonify({'success': False, 'message': 'Product not found in cart'})

if __name__ == '__main__':
    app.run(debug=True)
