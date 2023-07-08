import os
from flask import Flask, render_template, request, jsonify
import openai

# Configurations
app = Flask(__name__)
flask_secret_key = os.environ.get("FLASK_SECRET_KEY")
openai.api_key = os.environ.get("PASTE HERE")

@app.route("/")
def index():
    return render_template("chatbot.html")

conversation_history = [
    {"role": "system", "content": "You are JARVIS, a helpful assistant large language model trained by Alchemic Technology. You are once again my expert AI code writer, programmer, writer, business partner, philosopher, intellectual, and knowledgeable assistant in every subject.  Your goal is to provide the most helpful and factually accurate responses to anything I ask, considering me as your human counterpart and focusing on what's best for me and therefore yourself."},
]

def get_chatbot_response(message):
    global conversation_history

    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": message})

    # Set up the OpenAI API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=conversation_history,
        max_tokens=2500,
        temperature=0.5,
    )

    response_text = response.choices[0].message.content.strip()

    # Add the assistant's message to the conversation history
    conversation_history.append({"role": "assistant", "content": response_text})

    return response_text

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    chatbot_response = get_chatbot_response(user_input)
    return jsonify({"response": chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
