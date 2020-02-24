import random
from word_frequency import frequency, histogram

def sample_dict(histogram):
    '''Dictionary-type histogram for stochatic sampling
       Stochastic sampling takes an element from a given collection at random
       based on weight
       Then returns a random word
    '''
    word_count = 0
    word_count += sum(histogram[word] for word in histogram.keys()) # Calculates total word count in given text
    word_range=0
    histogram={}
    random_integer=random.random()

    for key in histogram.keys():
        histogram[key] = histogram[key] / word_count
        if random_integer > word_range and random_integer <= word_range + histogram[key]:
            return key
        word_range += histogram[key]


if __name__ == '__main__':
    filename = "words.txt"
    word_histogram = {}

    with open(filename, 'r') as f:
        words = f.read().split(' ')
        histogram = histogram(words)

    print(sample_dict(histogram))
        
        