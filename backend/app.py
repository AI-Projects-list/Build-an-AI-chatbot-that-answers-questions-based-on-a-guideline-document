from flask import Flask, request, jsonify
from chatbot import get_answer

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = get_answer(user_input)
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)