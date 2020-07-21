from data import Data
from auto_complete_methods import get_best_k_completions


def auto_complete(data):
    # curr_input = get_input() #generator of input
    result = get_best_k_completions(curr_input)
    # output(result)


auto_complete.last_input = ""


def terminal(data):
    while True:
        auto_complete(data)


def start_app(data):
    terminal(data)
