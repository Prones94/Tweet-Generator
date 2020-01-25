import os, random

def open_os():
    with open('/usr/share/dict/words', 'r') as f:
        word_list = f.readlines()
        f.close()

    return word_list

def choose_words(num):
    all_words = open_os()
    word_array = []
    for _ in range(num):
        word_array.append(random.choice(all_words)[:-3])
    return word_array

def show_words():
    num = int(input('How many words would you like to display? '))
    random_words = choose_words(num)
    print(' '.join(random_words)+'.')

show_words()

