from flask import (Flask, jsonify)

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World! This is dev!"


@app.route('/fancy_feature/<name>')
def home_name(name):
    return "Hello World! And hello to you too, {}!".format(name)


if __name__ == "__main__":
    app.run()
