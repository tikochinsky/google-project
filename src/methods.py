from data.data import Data, clean_string
from data.auto_complete_data import AutoCompleteData
import itertools

alphabet = "abcdefghijklmnopqrstuvwxyz "


def get_input():
    string = ""
    new_input = input(string)
    while new_input == "":
        new_input = input(string)
    while new_input == "" or new_input[len(new_input) - 1] != '#':
        string += clean_string(new_input)
        yield string
        new_input = input(string)


def find_completion(data, _input, score):
    best_completions = []
    result = data.get_substrings_dict().find(_input)
    for sentence_descriptor in result:
        best_completions.append(AutoCompleteData(data.get_sentences()[sentence_descriptor.get_id()][0],
                                                        data.get_sentences()[sentence_descriptor.get_id()][1],
                                                        sentence_descriptor.get_offset(), score))
    return best_completions


def find_replaced(data, _input, _index, num_required, score):
    result = []
    for ch in alphabet:
        for item in find_completion(data, _input[:_index]+ch+_input[_index+1:], score):
            result.append(item)
            if len(result) >= num_required:
                return result[:num_required]

    return result


def find_added(data, _input, _index, num_required, score):
    result = []
    for ch in alphabet:
        for item in find_completion(data, _input[:_index] + ch + _input[_index:], score):
            result.append(item)
            if len(result) >= num_required:
                return result[:num_required]

    return result


def find_deleted(data, _input, _index, num_required, score):
    result = []
    for item in find_completion(data, _input[:_index] + _input[_index+1:], score):
        result.append(item)
        if len(result) >= num_required:
            return result[:num_required]

    return result


def get_best_k_completions(data, _input, k):
    decrement_scores = {"find_replaced": [6, 5, 4, 3, 2],
                        "find_deleted": [11, 9, 7, 5, 3],
                        "find_added": [10, 8, 6, 4, 2]}
    flag_max = 20

    best_k_completions = set(find_completion(data, _input, len(_input)*2))

    if len(best_k_completions) < k:
        for _index in range(4, len(_input)):
            best_k_completions.update(find_replaced(data, _input, _index, k-len(best_k_completions), len(_input)*2 - 2))

            if len(best_k_completions) == k:
                break

    if len(best_k_completions) < k:
        for _index in range(4, len(_input)):
            best_k_completions.update(find_added(data, _input, _index, k-len(best_k_completions), len(_input)*2 - 2))

            if len(best_k_completions) == k:
                break

    if len(best_k_completions) < k:
        for _index in range(4, len(_input)):
            best_k_completions.update(find_deleted(data, _input, _index, k-len(best_k_completions), len(_input)*2 - 3))

            if len(best_k_completions) == k:
                break

    while len(best_k_completions) < k:
        curr_min = min(list(itertools.chain.from_iterable(decrement_scores.values())))
        if curr_min == flag_max: # or something that shows the dict has finished
            return best_k_completions

        for action, values in decrement_scores.items():
            if curr_min in values:
                index_of_min = values.index(curr_min)
                values[values.index(curr_min)] = flag_max
                best_k_completions.update(eval(action)(data, _input, index_of_min, k - len(best_k_completions),
                                                    len(_input)*2-curr_min))
                if len(best_k_completions) == k:
                    return best_k_completions

    return best_k_completions


def print_result(result):
    if len(result):
        print(f"Here are {len(result)} suggestions")
        for i, sentence in enumerate(result):
            print(str(i+1)+".", sentence.get_completed_sentence(), "(", sentence.get_sentence_source(), ")")
    else:
        print("No suggestions")




# decrement_scores = scores[:]
# curr_min = min(list(itertools.chain.from_iterable(decrement_scores.values())))
# for action, values in decrement_scores.items():
#     if curr_min in values:
#         index_of_min = values.index(curr_min)
#         values[values.index(curr_min)] = 20
#         # action with index...
#         best_k_completions += eval(action)(index_of_min, _input, k-len(best_k_completions))
#         break


# += [x for x in
#                                        eval(action)(data, _input, index_of_min, k - len(best_k_completions),
#                                                     len(_input)*2-curr_min)
#                                        if (x.get_completed_sentence(), x.get_sentence_source()) not in
#                                        [(y.get_completed_sentence(), y.get_sentence_source()) for y in
#                                         best_k_completions]]