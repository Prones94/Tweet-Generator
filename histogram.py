from __future__ import division, print_function
import re  # for changing lines to words list
from random import randint, choice, seed
seed(1)  # for different random numbers


class Histogram(dict):  # Creates Histogram class from dictionary
    def __init__(self, lines=None):  # lines is a string
        """Initializes this histogram as a new list and count given words"""
        super(Histogram, self).__init__()  # Initializes new list
        # Add properties to track useful word coutns for this histogram
        self.unique_word_count = 0  # Counts all unique words ## TYPES
        self.word_count = 0  # Total count of all words ## TOKENS
        self.words = []  # List of all words
        if lines != None:  # IF list != empty, this will update all count
            for line in lines:
                # Turns every word in line to a list of words
                words_from_line = re.sub("[^w]", "", line).split()
                for word in words_from_line:  # Loops through each word and returns histogram result
                    self.add_count(word)

    def add_count(self, word, count=1):
        """Increases frequency count of given word by given count amount"""
        if self.frequency(word) > 0:  # if word already exists
            self[word] += count
        else:
            self[word] = count
            self.unique_word_count += 1
        self.word_count += count

    def frequency(self, word):
        """Returns frequency count of a given word, if not found returns 0"""
        if not self.__contains__(word):
            return 0
        frequency = self[word]
        return frequency

    def get_count(self, word):
        word_count = 0
        for word in self:
            # IF word exits, word_count will increment by 1
            word_count = self.get(word, 0) + 1
            self[word] = word_count

    def __contains__(self, word):
        for word_history in self:
            if word == word_history:
                return True
        return False


def show_histogram(source_text):
    return Histogram(source_text)


def unique_words(histogram):
    return histogram.unique_words


def frequency_word(word, histogram):
    return histogram.frequency(word)


def contains_word(word, histogram):
    if histogram.__contains__(word):
        return True
    return False


if __name__ == "__main__":
    my_histogram = Histogram("one fish two fish red fish blue fish")
    print(f"Histogram = {my_histogram}")
    print(f'Unique word count: {my_histogram.unique_word_count}')
    print(f'Word count: {my_histogram.word_count}')
    word = "fish"
    contains_word = f"appears in {my_histogram.frequency(word)} times in " if contains_word(
        word, my_histogram) else "Cannot find"
    print(f"{word} {contains_word} in this histogram: {my_histogram}")
