import re
from get_words_dict import get_words_dict
from preprocess_text import preprocess_text
import statistics


def get_avd_and_median(input_text, sub_str):
    processed_text, unique_words = preprocess_text(input_text, sub_str)

    sentences = re.split(r'[.]{3}|[.]|[!]|[?]', processed_text)
    sentences = [re.sub(r'\n|\t', '', sentence) for sentence in sentences]
    processed_sentences = []

    for sentence in sentences:
        if sentence:
            processed_sentences.append(sentence)

    sentences = processed_sentences
    num_of_sentences = len(sentences)
    num_word_sen = []
    for sentence in sentences:
        word_dict, words_num = get_words_dict(sentence, False, sub_str, key=False)
        num_word_sen.append(words_num)

    avg_word = statistics.mean(num_word_sen)
    median_word = statistics.median(num_word_sen)
    return avg_word, median_word, num_of_sentences
