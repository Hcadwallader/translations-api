import re
from collections import OrderedDict
from spellchecker import SpellChecker

spell = SpellChecker()

def split_list(list, chunk_size):
    return [list[i:i + chunk_size] for i in range(0, len(list), chunk_size)]

def clean_words(words):
    return [clean_word(word) for word in words]

def clean_word(word):
    return re.sub(r'[^a-zA-Z]','',word)

def remove_duplicates(word_list):
    return list(OrderedDict.fromkeys(word_list))

def autocorrect_spelling_mistakes(word_list):
    list = [spell.correction(word) for word in word_list]
    return [x for x in list if x is not None] # Need this as it returns None if can't autocorrects

def cleanse_inputs(word_list):
    word_list = remove_duplicates(word_list)
    word_list = autocorrect_spelling_mistakes(word_list)
    word_list = clean_words(word_list)
    return remove_duplicates(word_list)