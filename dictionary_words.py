import os, random
import sys as sys
from python_quote import random_python_quote

def random_sentence(sentence_length, words):
    new_sentence = ""
    for _ in range(sentence_length):
        word = random_python_quote(words)
        new_sentence += word + " "
    return new_sentence

if __name__ == "__main__":
    with open('histogram.txt', 'r') as f:
        words = f.read().split(' ')
    
    sentence_length = int(sys.argv[1])
    print(sentence_length)
    print(random_sentence(sentence_length, words))





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

