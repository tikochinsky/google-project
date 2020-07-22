from data import Data, SubstringsDict, Sentences
from sentence import Sentence


def fill_sentences(data):
    sentences = data.get_sentences()
    sentences.insert("To be or not to be, that's the question", "dir1/dir2/file1")
    sentences.insert("We are waiting for it to work...", "dir3/file2")
    sentences.get_sentences().sort(key=lambda x: x.get_sentence())

    # the function of iterating over files
    # for each file:
    # split sentences
    # insert into sentences


def fill_substrings_dict(data):
    sentences = data.get_sentences().get_sentences()
    substrings_dict = data.get_substrings_dict()
    for i in range(len(sentences)):
        sentence = sentences[i].get_sentence()
        for j in range(len(sentence)):
            for k in range(j):
                substrings_dict.insert(sentence[k:j], i, k)

    print(substrings_dict.get_substrings_dict())


def manipulate_data(data):
    fill_sentences(data)
    fill_substrings_dict(data)
