

class AutoCompleteData:
    def __init__(self, completed_sentence, source_text, offset, score):
        self.__completed_sentence = completed_sentence
        self.__source_text = source_text
        self.__offset = offset
        self.__score = score

    def get_completed_sentence(self):
        return self.__completed_sentence

    def get_sentence_source(self):
        return self.__source_text

    def __key(self):
        return self.__completed_sentence, self.__source_text, self.__offset

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return self.__key() == other.__key()

    # methods that you need to define by yourself
