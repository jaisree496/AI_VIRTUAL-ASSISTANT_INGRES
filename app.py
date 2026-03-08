from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():

    user_input = request.form["msg"]

    prompt = f"""
You are an AI assistant for INGRES (Information and Guidance Response System).

Help users with:
- login problems
- service information
- complaint registration
- contacting support

User question: {user_input}
"""

    try:
        response = model.generate_content(prompt)
        reply = response.text

    except Exception as e:
        reply = "AI service unavailable."

    return jsonify(reply)

if __name__ == "__main__":
    app.run(debug=True)