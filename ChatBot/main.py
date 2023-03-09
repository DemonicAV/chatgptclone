import openai
from flask import Flask, render_template, request
from builtins import reversed


openai.api_key = "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"

app = Flask(__name__)
messages = []

def generate_response(prompt):
    model_engine = "text-davinci-002"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1000
    )
    message = response.choices[0].text.strip()
    return message

@app.route('/')
def home():
    return render_template('index.html', messages=messages)

@app.route('/', methods=['POST'])
def generate_text():
    user_input = request.form['user_input']
    prompt = f"You said: {user_input}\nAI says:"
    bot_response = generate_response(prompt)
    user_message = {'sender': 'user', 'text': user_input}
    bot_message = {'sender': 'bot', 'text': bot_response}
    messages.append(user_message)
    messages.append(bot_message)
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
