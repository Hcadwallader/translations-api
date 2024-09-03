from flask import Flask, request
from utilities import clean_words, remove_duplicates
from translation_api import call_translation_api


app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    target_language = request.json['targetLanguage']
    print(f'length of initial word list: {len(request.json['words'])}')
    word_list_without_duplicates = remove_duplicates(request.json['words'])
    print(f'length after remove duplicates: {len(word_list_without_duplicates)}')
    word_list = clean_words(word_list_without_duplicates)
    clean_list_without_duplicates = remove_duplicates(word_list)
    print(f'length after remove duplicates and clean: {len(clean_list_without_duplicates)}')
    return {
        'targetLanguage': target_language,
        'words': call_translation_api(target_language, word_list)
        }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)