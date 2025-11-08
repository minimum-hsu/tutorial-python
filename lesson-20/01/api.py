#!/usr/bin/env python3

from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template_string
from datetime import datetime

app = Flask(__name__)

# Simulated in-memory "database" of users
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

@app.route("/", methods=["GET"])
def home():
    html = """
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>Flask Home</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f9f9f9; }
            h1 { color: #333; }
            .info { margin-top: 20px; }
            code { background: #eee; padding: 3px 6px; }
        </style>
    </head>
    <body>
        <h1>Welcome to the Flask API Server!</h1>
        <p class="info">Current time: {{ time }}</p>
        <p>Available APIs:</p>
        <ul>
            <li><code>GET /api/users</code> - Get all users</li>
            <li><code>GET /api/users/&lt;id&gt;</code> - Get a specific user</li>
            <li><code>POST /api/users</code> - Add a new user</li>
        </ul>
    </body>
    </html>
    """
    return render_template_string(html, time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/api/users", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Missing name or email"}), 400

    new_id = max(u["id"] for u in users) + 1 if users else 1
    new_user = {"id": new_id, "name": data["name"], "email": data["email"]}
    users.append(new_user)
    return jsonify(new_user), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
