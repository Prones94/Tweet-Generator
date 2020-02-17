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

