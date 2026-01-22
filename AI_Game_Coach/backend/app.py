from flask import Flask, request, jsonify
from flask_cors import CORS
from coach_agent import generate_feedback

app = Flask(__name__)

# ✅ VERY IMPORTANT: allow GitHub Pages
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=["GET"])
def home():
    return "AI Game Coach Backend is Running 🚀"

# ✅ THIS is the API your frontend must call
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data:
        return jsonify({"feedback": "No input data received"}), 400

    feedback = generate_feedback(data)
    return jsonify({"feedback": feedback})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
