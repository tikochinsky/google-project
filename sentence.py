
class Sentence:
    def __init__(self, sentence, url):
        self.__sentence = sentence
        self.__url = url

    def get_sentence(self):
        return self.__sentence

    def get_url(self):
        return self.__url
