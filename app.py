from flask import Flask, request
from utilities import clean_words
from translation_api import call_translation_api


app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    target_language = request.json['targetLanguage']
    word_list = clean_words(request.json['words'])
    return {
        'targetLanguage': target_language,
        'words': call_translation_api(target_language, word_list)
        }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)