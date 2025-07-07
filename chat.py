from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Your Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-1.5-flash"

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")
        if not prompt:
            return jsonify({"response": "No input provided."})
        
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

@app.route("/")
def home():
    return "<h2>Gemini Chatbot API is Running.</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
