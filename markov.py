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

    def walk(self, num_words):
        # TODO: generate a sentence num_words long using the markov chain
        sentence = []
        random_key = [key for key in num_words.keys()]

        i = 0
        while i < 5:
            output = choice(random_key)
            sentence.append(output)
            i += 1

        return " ".join(sentence) 

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.dictionary_histogram)


markov_chain = MarkovChain(
    ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
markov_chain.print_chain()
print(markov_chain.walk(10))
