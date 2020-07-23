from data import Data, SubstringsDict, Sentences, clean_string
import os


def fill_sentences(data):
    sentences = data.get_sentences()
    print("loading the file and preparing the system...")
    # sentences.insert("To be or not to be, that's the question", "dir1/dir2/file1")
    # sentences.insert("We are waiting for it to work...", "dir3/file2")
    with open("technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/about.txt", encoding="utf8") as file:
        file_sentences = [line.rstrip() for line in file]
        for sentence in file_sentences:
            if sentence != '':
                sentences.insert(sentence, "technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/about.txt")

    # root_dir = 'technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/c-api'
    #
    # for subdir, dirs, files in os.walk(root_dir):
    #     for file in files:
    #         file_sentences = open(os.path.join(subdir, file), encoding="utf8").readlines()
    #         file_sentences = [line.rstrip() for line in file_sentences]
    #         for sentence in file_sentences:
    #             sentences.insert(sentence, os.path.join(subdir, file))

    sentences.get_sentences().sort(key=lambda x: x[0])
    print("finished loading")


def fill_substrings_dict(data):
    counter = 0
    sentences = data.get_sentences()
    substrings_dict = data.get_substrings_dict()
    print(sentences.get_sentences())
    for i, sentence in enumerate(sentences.get_sentences()):
        for j in range(1, len(sentence[0])):
            for k in range(j):
                substrings_dict.insert(clean_string(sentence[0][k:j]), i, k)
                print(counter)
                counter += 1

    print("finished loading")


def manipulate_data(data):
    fill_sentences(data)
    fill_substrings_dict(data)
