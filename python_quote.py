import random

def random_python_quote(word_list):
    random_index = random.randint(0, len(word_list) - 1)
    return word_list[random_index]

if __name__ == '__main__':
    quotes = ["It's just a flesh wound.",
              "He's not the Messiah. He's a very naughty boy!", "THIS IS AN EX-PARROT!!"]
    random_quote = random_python_quote(quotes)
    print(random_quote)
