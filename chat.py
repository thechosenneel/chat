from flask import Flask, request, jsonify, send_file
import google.generativeai as genai
import os

app = Flask(__name__)

# Gemini API Key
GEMINI_API_KEY = "AIzaSyDHHL0WlrPbL2tC9nVkZXJ6skbsElRQeTg"
MODEL_NAME = "gemini-1.5-flash"

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

@app.route("/")
def home():
    return send_file("gemini_chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        prompt = request.json.get("prompt", "")
        if not prompt:
            return jsonify({"response": "Please provide a prompt."})
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
