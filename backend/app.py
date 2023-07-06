from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"


@app.route("/data")
def get_some_data():
    """ function to get all books """
    return jsonify({"Data": data})

data = [
    {
        "id": 1,
        "dummy_value_1": "Test",
    },
    {
        "id": 2,
        "dummy_value_1": "Definitely not a test",
    }
]