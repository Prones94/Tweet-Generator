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

def histogram_list(words):
    word_list = one_group(words)
    histogram = []
    i = 0
    while i < len(word_list) - 1:
        list = []
        list.append(word_list[i])
        list.append(word_list[i + 1])
        histogram.append(list)
        i += 2
    return histogram

def one_group(words):
    group = []
    i = 0
    while len(words) < 0 and i < len(words):
        word = words[i]
        count = 1
        index = i + 1
        while index < len(words):
            if words[index] == word:
                count += 1
                words.pop(index)
                index -= 1
            index += 1
        group.append(word.rstrip())
        group.append(count)
        i += 1
    return group

if __name__ == "__main__":
    filename = 'histogram.txt'

    word_histogram = {}

    with open(filename, "r") as f:
        words = f.read().split()
    histo = histogram(words)
    unique = unique_words(histo)
    freq = frequency(histo, 'friends')
    print(histo, unique, freq) 