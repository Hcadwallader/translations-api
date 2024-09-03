import requests
from utilities import split_list


MAX_WORDS_IN_SINGLE_REQUEST = 100
LIBRE_URL = "http://localhost:7001"


def call_translation_api(target_language, full_list):
    chunked_lists = split_list(full_list, MAX_WORDS_IN_SINGLE_REQUEST)
    translations = []
    for chunk in chunked_lists:
        translations.extend(__call_translation_with_limited_list(target_language, chunk))
    return translations


def __call_translation_with_limited_list(target_language, words):
    translations = []
    request_data = {
        'q': words,
        'source': 'en',
        'target': target_language
        }

    libre_response = requests.post(f'{LIBRE_URL}/translate', json=request_data, headers={ "Content-Type": "application/json" })

    if libre_response.status_code == 200:
        libre_translated = libre_response.json()['translatedText']
        for index, translated in enumerate(libre_translated):
            translations.append({
                'originalWord': words[index],
                'translatedWord': translated
                })
    else:
        print(f'Unexpected status code: {libre_response.status_code}')

    return translations
