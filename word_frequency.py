import random

def histogram(words):
    histogram = {}
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1
    return histogram

def unique_words(histogram):
    return len(histogram)

def frequency(histogram, word):
    return histogram.get(word, False)

if __name__ == "__main__":
    filename = 'histogram.txt'

    word_histogram = {}

    with open(filename, "r") as f:
        words = f.read().split()
    histo = histogram(words)
    unique = unique_words(histo)
    freq = frequency(histo, 'friends')
    print(histo, unique, freq) 