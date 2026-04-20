from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_message = request.form["msg"]

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": user_message}] 
    )

    reply = response["message"]["content"]

    return reply

if __name__ == "__main__":
    app.run(debug=True)
