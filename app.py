from flask import Flask, jsonify

app = Flask(__name__)

def add_numbers(a, b):
    return a + b

@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "Hello Dr. Tariq, Project 2 is Ready!,Hello from GitHub Desktop.!"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)