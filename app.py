import os
import requests

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = Flask(_name_)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        if not GROQ_API_KEY:
            return jsonify({"error": "Groq API key is missing"}), 500

        data = request.get_json()
        message = data.get("message", "").strip()

        if not message:
            return jsonify({"error": "Please enter a message"}), 400

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.3-70b-versatile",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are CyberGPT, a helpful AI cybersecurity assistant."
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 1024
            },
            timeout=60
        )

        response.raise_for_status()

        answer = response.json()["choices"][0]["message"]["content"]

        return jsonify({
            "response": answer,
            "reply": answer
        })

    except requests.exceptions.RequestException:
        return jsonify({"error": "Unable to connect to Groq AI. Please try again."}), 502

    except Exception:
        return jsonify({"error": "Something went wrong. Please try again."}), 500
      
