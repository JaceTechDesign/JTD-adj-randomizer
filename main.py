from flask import Flask, jsonify
import random

app = Flask(__name__)

# Your list of random adjectives
responses = [
    "a red", "an orange", "a yellow", "a blue", "a green", "a purple", "a brown",
    "a black", "a white", "a pink", "a gray", "an indigo", "a turquoise", "a beige",
    "a teal", "a shitcovered", "a crooked", "a rockhard", "a razor-sharp",
    "a melted", "a teethmarked", "a smelly", "a dusty", "a slimy", "a dirty",
    "a blunt", "a jagged", "an unbreakable", "a fart-smelling", "a hateful",
    "a loving", "an uncivilized", "an unholy", "a delicious", "a tempting",
    "an attractive", "an ugly", "a vibrating", "a leather", "a sexy", "a hot",
    "an ice cold"
]

@app.route('/random', methods=['GET'])
def get_random_response():
    return jsonify(random.choice(responses))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
