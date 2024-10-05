from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot.intent_classifier import classify_intent
from chatbot.response_generator import generate_response
from chatbot.translator import translate_text

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    language = data.get('language', 'en')

    # Translate user message to English if not already in English
    if language != 'en':
        user_message = translate_text(user_message, source=language, target='en')

    # Classify intent
    intent = classify_intent(user_message)

    # Generate response
    response = generate_response(intent, user_message)

    # Translate response back to the user's language if needed
    if language != 'en':
        response = translate_text(response, source='en', target=language)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)