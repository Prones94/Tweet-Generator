from random import shuffle
from sys import argv

if __name__ == '__main__':
    args = argv[1:]
    shuffle(args)
    print(" ".join(args))