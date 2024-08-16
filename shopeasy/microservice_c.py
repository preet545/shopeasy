from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data.get('email') or not data.get('password'):
        return jsonify({"error": "Required fields are missing"}), 400

    if any(user['email'] == data['email'] for user in users):
        return jsonify({"error": "Email already registered"}), 400

    users.append({'email': data['email'], 'password': data['password'][::-1]})  # Simple encryption (reverse password)
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = next((user for user in users if user['email'] == data['email'] and user['password'] == data['password'][::-1]), None)
    if user:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5002)
