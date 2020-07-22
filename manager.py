from data import Data
from auto_complete_methods import get_best_k_completions, get_input, print_result


def auto_complete(data):
    for curr_input in get_input():
        result = get_best_k_completions(data, curr_input, 5)
        print_result(result)


auto_complete.last_input = ""


def terminal(data):
    while True:
        auto_complete(data)


def start_app(data):
    terminal(data)
