from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'

products = [
    {"id": 1, "name": "iPhone 14 Pro Max", "price": 999, "description": "The Apple iPhone 14 Pro Max features a stunning 6.7-inch Super Retina XDR display, the powerful A16 Bionic chip, and an advanced triple-camera system for professional-grade photography.", "image": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/refurb-iphone-14-pro-max-spaceblack-202404?wid=1144&hei=1144&fmt=jpeg&qlt=90&.v=1713200628539"},
    {"id": 2, "name": "Airpods", "price": 250, "description": "Airpods provide a seamless and wireless audio experience with high-quality sound.", "image": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6376/6376551cv13d.jpg;maxHeight=2000;maxWidth=2000"},
    {"id": 3, "name": "Airpods ProMax", "price": 600, "description": "The Apple AirPods Max offer a premium over-ear listening experience with high-fidelity audio, active noise cancellation, and spatial audio.", "image": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6446/6446644_sd.jpg;maxHeight=640;maxWidth=550"},
    {"id": 4, "name": "MacBook Air 15'", "price": 1200, "description": "The Apple MacBook Air 15' boasts a larger display, the powerful M2 chip, and an ultra-thin design.", "image": "https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6565/6565835_sd.jpg;maxHeight=640;maxWidth=550"},
]

users = []
cart = []

@app.route('/')
def home():
    cart_count = len(cart)
    return render_template('index.html', products=products, cart_count=cart_count)

@app.route('/products')
def product_list():
    cart_count = len(cart)
    return render_template('products.html', products=products, cart_count=cart_count)

@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    cart_count = len(cart)
    return render_template('product_detail.html', product=product, cart_count=cart_count)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        response = requests.post("http://localhost:5000/register", json={"email": email, "password": password})
        if response.status_code == 201:
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Registration failed. Email may already be registered.', 'danger')
    cart_count = len(cart)
    return render_template('register.html', cart_count=cart_count)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        response = requests.post("http://localhost:5000/login", json={"email": email, "password": password})
        if response.status_code == 200:
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Invalid email or password.', 'danger')
    cart_count = len(cart)
    return render_template('login.html', cart_count=cart_count)

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        response = requests.post("http://localhost:5000/reset_password", json={"email": email})
        if response.status_code == 200:
            flash('Password reset email sent!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Password reset failed. Email may not be registered.', 'danger')
    cart_count = len(cart)
    return render_template('reset_password.html', cart_count=cart_count)

@app.route('/cart')
def view_cart():
    total = sum(item['price'] for item in cart)
    cart_count = len(cart)
    return render_template('cart.html', cart=cart, total=total, cart_count=cart_count)

@app.route('/checkout')
def checkout():
    cart_count = len(cart)
    return render_template('checkout.html', cart_count=cart_count)

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"message": "Product not found"}), 404

@app.route('/api/cart', methods=['POST'])
def add_to_cart():
    product_id = request.json.get('product_id')
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        cart.append(product)
        return jsonify({"message": "Product added to cart", "cart_count": len(cart)}), 201
    return jsonify({"message": "Product not found"}), 404

@app.route('/api/cart/remove', methods=['POST'])
def remove_from_cart():
    product_id = request.json.get('product_id')
    global cart
    cart = [item for item in cart if item["id"] != product_id]
    return jsonify({"message": "Product removed from cart", "cart_count": len(cart)}), 200

if __name__ == '__main__':
    app.run(debug=True, port=8000)
