from __future__ import division, print_function
from random import randint, choice, seed
seed(1)
import re

class Histogram(dict):
    def __init__(self, lines=None):
        super(Histogram, self).__init__()
        self.unique_words_count = 0
        self.word_count = 0
        self.words = []
        if lines != None:
            for line in lines:
                words_from_line = re.sub("[^w]", "", line).split()
                for word in words_from_line:
                    self.add_count(word)

    def add_count(self, word, count=1):
        if self.frequency(word) > 0:
            self[word] += count
        else:
            self[word] = count
            self.unique_words_count += 1
        self.word_count += count

    def get_count(self, word):
        word_count = 0
        for word in self:
            word_count = self.get(word, 0) + 1
            self[word] = word_count
    
    def frequency(self, word):
        if not self.__contains__(word):
            return 0
        frequency = self[word]
        return frequency
    
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
    print(f'Unique word count: {my_histogram.word_count}')
    print(f'Word count: {my_histogram.word_count}')
    word = "fish"
    contains_word = f"appears in {my_histogram.frequency(word)} times in " if   contains_word(word, my_histogram) else "Cannot find"
    print(f"{word} {contains_word} in this histogram: {my_histogram}")