from flask import Flask, request, jsonify, render_template
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    to_translate = data.get('text')
    translated = GoogleTranslator(source='auto', target='en').translate(to_translate)
    return jsonify({'translated_text': translated})

if __name__ == '__main__':
    app.run(debug=True)
