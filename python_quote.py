import random

def random_python_quote(quotes):
    random_index = random.randint(0, len(quotes) - 1)
    return quotes[random_index]

if __name__ == '__main__':
    quotes = [
    "It's just a flesh wound",
    "He's not the Messiah. He's a very naughty boy!",
    "THIS IS AN EX-PARROT!!"
    ]
    words = random_python_quote(quotes)
    print(words)
