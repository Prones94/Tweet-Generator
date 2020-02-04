def show_histogram():
    filename = 'histogram.txt'
    with open(filename, 'r') as f:
        lines = f.read().split()
    dictionary = {}
    for word in lines:
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

def unique_words(show_histogram):
    count = 0
    for word in show_histogram.keys():
        if show_histogram.get(word) == 1:
            count += 1

def frequency_word(word, show_histogram):
    return show_histogram.get(word)

def histogram_list():
    filename = "/Users/admin/Desktop/MAKE/CS/CS-1.2-Intro-Data-Structures/CS1.2/Tweet-Generator/histogram.txt"
    with open(filename, 'r') as f:
        lines = f.read().split()
        list_histogram = {}
        for word in lines:
            word_count = list_histogram.get(word, 0)
            list_histogram[word] = word_count + 1
    return list_histogram

if __name__ == "__main__":
    stored_histo_list = histogram_list()
    print(stored_histo_list)
    # print(frequency_word('for', stored_histo_list))
