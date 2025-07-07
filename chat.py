from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__, static_folder="static", template_folder="templates")

# Your Gemini API key
GEMINI_API_KEY = "AIzaSyDHHL0WlrPbL2tC9nVkZXJ6skbsElRQeTg"
MODEL_NAME = "gemini-1.5-flash"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        prompt = request.json.get("prompt", "")
        if not prompt:
            return jsonify({"response": "Please provide a valid prompt."})
        
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
