from get_words_dict import get_words_dict
import collections
import copy


def find_n_grams(N, K, input_text, sub_str):
    word_dict, words_num = get_words_dict(input_text, True, sub_str)
    n_gram = []
    for key, value in word_dict.items():
        if len(key) >= N:
            for i in range(len(key) - N + 1):
                for _ in range(value):
                    n_gram.append(key[i: i + N])

    counter = collections.Counter(n_gram)
    n_gram = copy.deepcopy(counter)
    n_gram_sorted = sorted(n_gram.items(), key=lambda item: item[1], reverse=True)

    return n_gram_sorted[0: K]
