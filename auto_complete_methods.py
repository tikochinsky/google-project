from data import Data
from auto_complete_data import AutoCompleteData
from data import clean_string, alphabet
import time
import itertools

scores = {"find_replaced": [6, 5, 4, 3, 2],
          "find_deleted": [11, 9, 7, 5, 3],
          "find_added": [10, 8, 6, 4, 2]}


def get_input():
    string = ""
    new_input = input(string)
    while new_input == "":
        new_input = input(string)
    while new_input == "" or new_input[len(new_input) - 1] != '#':
        string += clean_string(new_input)
        yield string
        new_input = input(string)


def find_replaced(index, _input, num_required):



def get_best_k_completions(data, _input, k):
    start_time = time.time()
    best_k_completions = []

    result = data.get_substrings_dict().find(_input)
    for sentence_descriptor in result:
        score = len(_input)*2
        best_k_completions.append(AutoCompleteData(data.get_sentences()[sentence_descriptor.get_id()][0],
                                                        data.get_sentences()[sentence_descriptor.get_id()][1],
                                                        sentence_descriptor.get_offset(), score))

    decrement_scores = scores[:]
    while len(best_k_completions) < k:
        curr_min = min(list(itertools.chain.from_iterable(decrement_scores.values())))
        for action, values in decrement_scores.items():
            if curr_min in values:
                index_of_min = values.index(curr_min)
                values[values.index(curr_min)] = 20
                # action with index...
                best_k_completions += eval(action)(index_of_min, _input, k-len(best_k_completions))
                break



    print("--- %s seconds ---" % (time.time() - start_time))
    return best_k_completions


def print_result(result):
    print("Here are 5 suggestions")
    for i, sentence in enumerate(result):
        print(str(i+1)+".", sentence.get_completed_sentence(), "(", sentence.get_sentence_source(), ")")
