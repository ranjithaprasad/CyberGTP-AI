
import os
import requests

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

@app.route("/")
def home():
    return jsonify({
        "name": "CyberGTP AI",
        "status": "Running",
        "message": "Welcome to your AI assistant!"
    })

@app.route("/chat", methods=["POST"])
def chat():
    if not GROQ_API_KEY:
        return jsonify({
            "error": "AI API key is not configured."
        }), 503

    data = request.get_json(silent=True) or {}
    messages = data.get("messages", [])

    if not isinstance(messages, list) or not messages:
        return jsonify({
            "error": "Please provide a message."
        }), 400

    conversation = [
        {
            "role": "system",
            "content": (
                "You are CyberGTP AI, a helpful cybersecurity "
                "assistant. Explain cybersecurity, networking, "
                "SOC analysis, ethical hacking and security "
                "concepts clearly. Support authorized and "
                "defensive security work. Never assist with "
                "unauthorized attacks."
            )
        }
    ]

    for message in messages[-10:]:
        if (
            isinstance(message, dict)
            and message.get("role") in ["user", "assistant"]
            and isinstance(message.get("content"), str)
        ):
            conversation.append({
                "role": message["role"],
                "content": message["content"][:4000]
            })

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-oss-20b",
                "messages": conversation,
                "temperature": 0.7,
                "max_completion_tokens": 1024
            },
            timeout=60
        )

        response.raise_for_status()
        result = response.json()

        return jsonify({
            "reply": result["choices"][0]["message"]["content"]
        })

    except requests.RequestException:
        return jsonify({
            "error": "AI service is temporarily unavailable."
        }), 502

    except (KeyError, IndexError, ValueError):
        return jsonify({
            "error": "Unable to process the AI response."
        }), 502


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
    
