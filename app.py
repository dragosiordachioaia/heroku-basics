from flask import (Flask, jsonify)

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "You need to request a resource"}), 404
