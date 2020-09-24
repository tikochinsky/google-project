from data.data import Data
from initialization import manipulate_data
from manager import start_app


if __name__ == '__main__':
    data = Data()
    manipulate_data(data)
    start_app(data)
