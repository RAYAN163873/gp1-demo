from flask import Flask, jsonify

app = Flask(__name__)

def add_numbers(a, b):
    return a + b

@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "Hello from gp1-demoo!Version 2.0 works!"})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # nosec