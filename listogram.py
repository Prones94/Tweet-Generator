#!python

from __future__ import division, print_function # Python 2 & 3 compatibility
from random import randint

class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type"""

    def __init__(self, word_list = None):
        """
        Initializes histogram as a new list and gives a count of words within file
        """
        super(Listogram, self).__init__()
        self.types = 0
        self.tokens = 0
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count = 1):
        index = self.index_of(word)
        if index is not None:
            old_count = self[index][1]
            new_count = old_count + count
            self[index] = (word, new_count)
        else:
            self.append((word, count))
            self.types += 1
        self.tokens += count
    
    def frequency(self, word):
        for item in self:
            if item[0] == word:
                return item[1]
        return 0

    def __contains__(self, word):
        for item in self:
            if word == item[0]:
                return True
        return False
    
    def index_of(self, target):
        for item in self:
            if item[0] == target:
                return self.index(item)
        return None

    def sample(self):
        total_count = 0
        for word_list in self:
            total_count += word_list[1]
        random_num = randint(0, total_count -1)
        random_weighted_word = ""
        for word_list in self:
            if random_num == 0:
                random_weighted_word = word_list[0]
                break
            if random_num > 0:
                random_num -= word_list[1]
            if random_num < 0:
                random_weighted_word = word_list[0]
                break
        random_num = randint(0, total_count - 1)
        return random_weighted_word

def print_gram(word_list):
    print("Histogram stats")
    print('List of words: {}'.format(word_list))
    histogram = Listogram(word_list)
    print('Listogram: {}'.format(histogram))
    for word in word_list[-2:]:
        frequency = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, frequency))
    print()
    print_samples(histogram)

def print_samples(histogram):
    print('Histogram samples:')
    sample_listo = [histogram.sample() for _ in range (10000)]
    sample_histo = Listogram(sample_listo)
    print('Sample: {}'.format(sample_histo))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed frequency | sampled frequency | error |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Color coordinated for different errors
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Checks for each word in original histogram
    for word, count in histogram:
        observed_frequency = count / histogram.tokens
        samples = sample_histo.frequency(word)
        sampled_frequency = samples / sample_histo.tokens
        error = (sampled_frequency - observed_frequency) / observed_frequency
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:6.2%} '.format(count, observed_frequency)
            + '| {:>4} = {:6.2%} '.format(samples, sampled_frequency)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
        print(divider)
        print()

def main():
    import sys
    arguments = sys.argv[1:]
    if len(arguments) >= 1:
        print_gram(arguments)
    else:
        word = 'abracadabra'
        print_gram(list(word))
        fish_text = 'one fish two fish red fish blue fish'
        print_gram(fish_text.split())
        woodchuck_text = ('how much wood would a wood chuck chuck'
                            ' if a wwood chuck could chuck wood')
        print_gram(woodchuck_text.split())

if __name__ == '__main__':
    main()

    