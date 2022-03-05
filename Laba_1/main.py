from find_n_grams import find_n_grams
from constants import sub_str
from get_avd_and_median import get_avd_and_median
from get_words_dict import get_words_dict

if __name__ == "__main__":
    text = input()
    N = int(input())
    K = int(input())
    word_dict, num_words = get_words_dict(text, True, sub_str)
    print(f"Word dict is : \n{word_dict}")

    avg_word, median_word, num_of_sentences = get_avd_and_median(text, sub_str)
    print(f"{num_of_sentences} sentences")
    print(f"Average number of words in a sentence: {avg_word}")
    print(f"Median: {median_word}")

    n_gram = find_n_grams(N, K, text, sub_str)
    print(f"N-gram:\n{n_gram}")
