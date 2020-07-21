from data import Data


def clean_string(_input):
    pass


def get_input():
    string = ""
    new_input = input()
    while new_input == "":
        new_input = input()
    while new_input[len(new_input)-1] != "#":
        string += clean_string(new_input)
        yield string


def get_best_k_completions(last_input):
    pass


# output(result)