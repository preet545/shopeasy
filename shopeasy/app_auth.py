from flask import Flask, request, jsonify, session, redirect, url_for
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

users = {}

@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    if email in users:
        return jsonify({"message": "Email already registered"}), 400
    hashed_password = generate_password_hash(password)
    users[email] = hashed_password
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    user_password = users.get(email)
    if user_password and check_password_hash(user_password, password):
        session['user'] = email
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({"message": "Logout successful"}), 200

@app.route('/reset_password', methods=['POST'])
def reset_password():
    email = request.json.get('email')
    if email not in users:
        return jsonify({"message": "Email not registered"}), 400
    # To send a email with the reset link 
    return jsonify({"message": "Password reset link sent"}), 200

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = 1800 

if __name__ == '__main__':
    app.run(debug=True, port=5000)
