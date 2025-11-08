#!/usr/bin/env python3

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(message="Hello Flask!")

if __name__ == "__main__":
    app.run(debug=True)
