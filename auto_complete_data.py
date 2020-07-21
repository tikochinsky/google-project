class AutoCompleteData:
    def __init__(self, completed_sentence, source_text, offset, score):
        self.__completed_sentence = completed_sentence
        self.__source_text = source_text
        self.__offset = offset
        self.__score = score

    # methods that you need to define by yourself
