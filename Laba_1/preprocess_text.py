import re
from constants import abbreviations, up_reg


def preprocess_text(input_text, sub_str):
    input_text = input_text + "\t."
    pattern = ""
    for abbreviation in abbreviations:
        abbreviation = abbreviation[: -1] + "[.]|"
        pattern += abbreviation
    pattern = pattern[: -1]

    abbreviation_arr = re.findall(pattern, input_text)
    input_text = re.sub(pattern, sub_str + "  ", input_text)

    word_arr = re.findall(r'\w+[.][a-z]\S+|\w+[.][a-z]', input_text)
    input_text = re.sub(r'\w+[.][a-z]\S+|\w+[.][a-z]', sub_str, input_text)
    word_arr += abbreviation_arr

    left_border = 0
    right_border = 0
    while left_border != -1:
        left_border = input_text.find(sub_str, right_border, len(input_text))
        right_border = left_border + len(sub_str)
        if input_text[right_border + 1] in up_reg:
            input_text = input_text[: right_border] + '.' + input_text[right_border + 1:]

    return input_text, word_arr
