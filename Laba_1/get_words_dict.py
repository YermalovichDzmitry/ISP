import re
import copy
from preprocess_text import preprocess_text
import collections


def get_words_dict(input_text, preprocess, sub_str, key=True):
    unique_words = []
    if preprocess:
        input_text, unique_words = preprocess_text(input_text, sub_str)

    words = re.findall(r'\w+', input_text)
    words += unique_words
    if key:
        words = [word for word in words if word != sub_str]

    counter = collections.Counter(words)
    word_dict = copy.deepcopy(counter)
    for key, value in counter.items():
        res = re.findall(r'\d', key)
        if res:
            word_dict.pop(key)

    num_words = 0
    for key, value in word_dict.items():
        num_words += value

    return word_dict, num_words
