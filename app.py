from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_cors import CORS
import pandas as pd
import os
import requests
from huggingface_hub import InferenceClient
import time
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Enable CORS for all routes
CORS(app)

# Initialize the Hugging Face Inference client
# You can set your API key here or use an environment variable
HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY", "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")
llama_client = InferenceClient(api_key=HUGGINGFACE_API_KEY)

# Llama 4 chat completion function (reference: chat_llama.py)
def get_chatbot_response(prompt: str, retries: int = 3, wait: float = 1.0) -> str:
    """
    Sends a prompt to the Llama 4 Scout model and returns the generated response.
    Retries on failure with exponential backoff.
    """
    for attempt in range(retries):
        try:
            response = llama_client.chat_completion(
                model="meta-llama/Llama-4-Scout-17B-16E-Instruct",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=350,
                top_p=0.9,
            )
            return response.choices[0].message["content"].strip()
        except Exception as e:
            print(f"[Chatbot Error Attempt {attempt + 1}] {e}")
            time.sleep(wait * (2 ** attempt))  # Exponential backoff
    return "Sorry, I'm having trouble generating a response right now. Please try again later."

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
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    reply = get_chatbot_response(prompt)
    return jsonify([{"generated_text": reply}])

@app.route('/product/<product_id>')
def product_details(product_id):
    product = next((p for p in products if p['product_id'] == product_id), None)
    if product is None:
        return redirect(url_for('product_listing'))
    return render_template('productdetails.html', product=product, products=products)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    cart_products = []
    total = 0

    for item in cart_items:
        product = next((p for p in products if str(p['product_id']) == str(item['product_id'])), None)
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

    product = next((p for p in products if str(p['product_id']) == str(product_id)), None)
    if not product:
        return jsonify({'success': False, 'message': 'Product not found'})

    cart = session['cart']
    existing_item = next((item for item in cart if str(item['product_id']) == str(product_id)), None)

    if existing_item:
        existing_item['quantity'] += quantity
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
                if quantity > 0:
                    item['quantity'] = quantity
                    session.modified = True
                    return jsonify({'success': True, 'message': 'Cart updated'})
                else:
                    return jsonify({'success': False, 'message': 'Quantity must be greater than 0'})

    return jsonify({'success': False, 'message': 'Product not found in cart'})

@app.route('/test')
def test():
    return render_template('test.html')
    
if __name__ == '__main__':
    app.run(debug=True)
