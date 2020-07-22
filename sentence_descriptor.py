class SentenceDescriptor:
    def __init__(self, id, offset):
        self.__sentence_id = id
        self.__sentence_offset = offset

    def get_id(self):
        return self.__sentence_id

    def get_offset(self):
        return self.__sentence_offset
