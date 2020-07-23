from data import Data
from auto_complete_methods import get_best_k_completions, get_input, print_result
import time


def terminal(data):
    while True:
        for curr_input in get_input():
            start_time = time.time()
            result = get_best_k_completions(data, curr_input, 5)
            print("--- %s seconds ---" % (time.time() - start_time))
            print_result(result)


def start_app(data):
    terminal(data)
