from dictogram import Dictogram
from random import choice, randint


class MarkovChain:
    def __init__(self, world_list):
        # The Markov chain will be a dictionary of dictograms
        # Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
        self.markov_chain = self.build_markov(world_list)
        self.first_word = list(self.markov_chain.keys())[0]

    def build_markov(self, word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1):
            # get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i + 1]

            if current_word in markov_chain.keys():  # word already in markov chain
                histogram = markov_chain[current_word]  # add to count
                histogram.dictionary_histogram[next_word] = histogram.dictionary_histogram.get(
                    next_word, 0) + 1
            else:
                markov_chain[current_word] = Dictogram([next_word])
        return markov_chain

    def random_word(self):
        word = choice(list(self.markov_chain.keys()))
        return word

    def walk(self, num_words):
        # TODO: generate a sentence num_words long using the markov chain
        sentence = ""
        first_word = self.random_word()
        print('The first word is ' + first_word)
        sentence += first_word + " "

        index = 0
        while index < num_words:
            current_word = first_word
            for word, histogram in self.markov_chain.items():
                if current_word == word:
                    word_in_dictogram = histogram.dictionary_histogram
                    print('From this word: ' + word + ". Dictogram sample will be " + word_in_dictogram)
                    weighted_random_word = histogram.sample()
                    print('This sample is' + weighted_random_word)
                    current_word = weighted_random_word
                    if index == num_words - 1:
                        sentence += current_word + '.'
                    else:
                        sentence += current_word + ' '
                    break
                else:
                    continue
            index += 1
        print('This sentence will be: ' + sentence)
    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.dictionary_histogram)


markov_chain = MarkovChain(
    ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
markov_chain.print_chain()
print(markov_chain.walk(10))
