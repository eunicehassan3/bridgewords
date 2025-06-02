from flask import Flask, render_template, request, jsonify
from game import get_random_word_pair, is_valid_word, is_related

# Global game state
START_WORD = ""
TARGET_WORD = ""
CURRENT_WORD = ""

# START_WORD, TARGET_WORD = get_random_word_pair()
# CURRENT_WORD = START_WORD 

with open("words/common_words.txt") as f:
    COMMON_WORDS = [word.strip().lower() for word in f if word.strip()]


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
# def index():
#     return jsonify({
#         "start": START_WORD,
#         "target": TARGET_WORD
#     })


@app.route("/play", methods=["POST"])
def play():
    global CURRENT_WORD  # Needed to update state
    data = request.get_json()
    guess = data.get("word", "").strip().lower()

    if not is_valid_word(guess):
        return jsonify(valid=False, message="❌ Not a real word.")

    if not is_related(CURRENT_WORD, guess):
        return jsonify(valid=False, message=f"⚠️ '{guess}' is not related to '{CURRENT_WORD}'.")

    CURRENT_WORD = guess
    goal_reached = CURRENT_WORD == TARGET_WORD
    return jsonify(valid=True, message=f"⚠️ '{guess}' is related to '{CURRENT_WORD}'.")
    # return jsonify(valid=True, message="✅ Good bridge!", goal=goal_reached)


@app.route("/get-words")
def get_words():
    global START_WORD, TARGET_WORD, CURRENT_WORD
    START_WORD, TARGET_WORD = get_random_word_pair()
    CURRENT_WORD = START_WORD
    return jsonify({
        "start": START_WORD,
        "target": TARGET_WORD
    })


@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    guess = data.get("word", "").lower()
    CURRENT_WORD = start

    if not is_valid_word(guess):
        return jsonify(valid=False, message="Not a real word.")
    
    if not is_related(CURRENT_WORD, guess):
        return jsonify(valid=False, message=f"⚠️ '{guess}' is not related to '{CURRENT_WORD}'.")

    CURRENT_WORD = guess
    goal_reached = CURRENT_WORD == TARGET_WORD
    return jsonify(valid=True, message=f"⚠️ '{guess}' is related to '{CURRENT_WORD}'.")


if __name__ == "__main__":
    app.run(debug=True)