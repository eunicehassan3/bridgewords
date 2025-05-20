from flask import Flask, render_template, request, jsonify
import random


app = Flask(__name__)

with open("words.txt") as f:
    WORDS = set(word.strip().lower() for word in f)

@app.route("/")
def index():
    start = "fire"
    target = "hospital"
    return render_template("index.html", start=start, target=target)

@app.route("/validate", methods=["POST"])
def validate():
    data = request.json
    word = data.get("word", "").lower()
    return jsonify(valid=word in WORDS)

if __name__ == "__main__":
    app.run(debug=True)