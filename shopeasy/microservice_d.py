from flask import Flask, request, jsonify

app = Flask(__name__)

cart = []

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.json
    if not data.get('product_id') or not data.get('name') or not data.get('price'):
        return jsonify({"error": "Required fields are missing"}), 400

    cart.append({
        "product_id": data['product_id'],
        "name": data['name'],
        "price": data['price']
    })
    return jsonify({"message": "Product added to cart"}), 201

@app.route('/view_cart', methods=['GET'])
def view_cart():
    total = sum(item['price'] for item in cart)
    return jsonify({"cart": cart, "total": total}), 200

@app.route('/checkout', methods=['POST'])
def checkout():
    if not cart:
        return jsonify({"error": "Cart is empty"}), 400
    cart.clear()
    return jsonify({"message": "Checkout successful"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5003)
