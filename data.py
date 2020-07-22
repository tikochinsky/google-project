from sentence import Sentence
from sentence_descriptor import SentenceDescriptor


# list of Sentences
class Sentences:
    def __init__(self):
        self.__sentences = []

    def insert(self, string, url):
        self.__sentences.append(Sentence(string, url))

    def get_sentences(self):
        return self.__sentences

    def __getitem__(self, key):
        return self.__sentences[key]


# dict of SentenceDescriptors
class SubstringsDict:
    def __init__(self):
        self.__dict = {}

# returns list of autoCompleteData
    def find(self, string):
        return self.__dict.get(string)

    def insert(self, key, sentence_id, substring_offset):
        if self.__dict.get(key):
            if len(self.__dict[key]) < 5:
                if sentence_id not in [sentence_descriptor.get_id() for sentence_descriptor in self.__dict[key]]:
                    self.__dict[key].append(SentenceDescriptor(sentence_id, substring_offset))
        else:
            self.__dict[key] = [SentenceDescriptor(sentence_id, substring_offset)]

    def get_substrings_dict(self):
        return self.__dict


class Data:
    def __init__(self):
        self.__sentences = Sentences()
        self.__substrings_dict = SubstringsDict()

    def get_sentences(self):
        return self.__sentences

    def get_substrings_dict(self):
        return self.__substrings_dict
