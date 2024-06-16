from flask import Flask, request, jsonify
from openai import OpenAI
import config

# set openai api key
client = OpenAI(
    api_key=config.OPENAI_API_KEY
)

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

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