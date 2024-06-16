from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import config

# set openai api key
client = OpenAI(
    api_key=config.OPENAI_API_KEY
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role":"user", "content":userText}
        ]
    )
    answer = response.choices[0].message.content
    return str(answer)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("input")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role":"user", "content":user_input}
        ]
    )
    answer = response.choices[0].message.content
    return jsonify({"response":answer})

if __name__ == "__main__":
    app.run()