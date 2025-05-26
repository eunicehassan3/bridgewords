from flask import Flask, render_template, request, jsonify
from game import get_random_word_pair, is_valid_word, is_related


app = Flask(__name__)


@app.route("/")


@app.route("/play", methods=["POST"])


if __name__ == "__main__":
    app.run(debug=True)