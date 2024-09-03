import re

def split_list(list, chunk_size):
    return [list[i:i + chunk_size] for i in range(0, len(list), chunk_size)]

def clean_words(words):
    return [clean_word(word) for word in words]

def clean_word(word):
    return re.sub(r'[^a-zA-Z]','',word)