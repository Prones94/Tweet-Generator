import random
import sys 
from python_quote import random_python_quote

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naught boy!",
          "ThIS IS AN EX-PARROT!!")

def random_sentence(sentence_length, words):
    new_sentence = ""
    for _ in range(sentence_length):
        word = random_python_quote()
        new_sentence += word + " "
    return new_sentence

if __name__ == "__main__":
    with open('histogram.txt', 'r') as f:
        words = f.read().split(' ')
    
    sentence_length = int(sys.argv[1])
    print(sentence_length)
    print(random_sentence(sentence_length, words))

