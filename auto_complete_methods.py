from data import Data
from auto_complete_data import AutoCompleteData

def clean_string(_input):
    # clean
    return _input


def get_input():
    string = ""
    new_input = input()
    while new_input == "":
        new_input = input()
    while new_input == "" or new_input[len(new_input) - 1] != '#':
        string += clean_string(new_input)
        yield string
        new_input = input()


def get_best_k_completions(data, _input, k):
    result = data.get_substrings_dict().find(_input)
    best_k_completions = []
    try:
        for sentence_descriptor in result:
            score = len(_input)*2
            best_k_completions.append(AutoCompleteData(data.get_sentences()[sentence_descriptor.get_id()],
                                                       _input, sentence_descriptor.get_offset(), score))

    except TypeError:
        return {}

    return best_k_completions


def print_result(result):
    for sentence in result:
        print(sentence.get_completed_sentence(), end=" ")
        print("(", sentence.get_sentence_url(), ")")
