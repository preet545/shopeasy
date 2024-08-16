from flask import Flask, request, jsonify

app = Flask(__name__)

product_catalog = [
    {"id": 1, "name": "iPhone 14 Pro Max", "price": 999},
    {"id": 2, "name": "Airpods", "price": 250},
]

@app.route('/get_product_catalog', methods=['GET'])
def get_product_catalog():
    return jsonify(product_catalog)

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    if not data.get('name') or not data.get('price'):
        return jsonify({"error": "Required fields are missing"}), 400

    new_product = {
        "id": len(product_catalog) + 1,
        "name": data["name"],
        "price": data["price"],
    }
    product_catalog.append(new_product)
    return jsonify({"message": "Product added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)
