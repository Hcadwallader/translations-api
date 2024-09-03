import re
from collections import OrderedDict

def split_list(list, chunk_size):
    return [list[i:i + chunk_size] for i in range(0, len(list), chunk_size)]

def clean_words(words):
    return [clean_word(word) for word in words]

def clean_word(word):
    return re.sub(r'[^a-zA-Z]','',word)

def remove_duplicates(word_list):
    return list(OrderedDict.fromkeys(word_list))