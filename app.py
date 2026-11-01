
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "name": "CyberGTP AI",
        "status": "Backend running",
        "message": "Welcome to CyberGTP AI!"
    })

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    return jsonify({
        "reply": "Your message received: " + user_message
    })

if __name__ == "__main__":
    app.run(debug=True)
