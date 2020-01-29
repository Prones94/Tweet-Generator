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
            count +=1

def frequency_word(word, show_histogram):
    return show_histogram.get(word)

def histogram_list():
    filename = "histogram.txt"
    with open(filename, 'r') as f:
        lines = f.read().split()
    list_histogram = []
    for word in lines:
        list_of_words = [word,0]
        for word_two in lines:
            if word == word_two:
                list_histogram[1] += 1
        if list_of_words not in list_histogram:
            list_histogram.append(list_histogram)
    return list_histogram

if __name__ == "__main__":
    stored_histo_list = histogram_list()
    print(frequency_word('for', stored_histo_list))
