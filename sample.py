import random
histogram = [('cats', 3), ('dogs', 4), ('rabbit', 2), ('turtles', 1)]


def sample(histogram):
    """Return a word from this histogram randomly sampled by weighting
    each word's probability of being chosen by its observed frequency."""
    tokens = sum([count for word, count in histogram])  # Count total tokens
    # Throw a dart on the number line
    dart = random.randint(1, tokens)
    # NOTE: Assume that randint returns 8 here and dart stores the value 8
    # Border of where each word splits the number line
    fence = 0
    for word, count in histogram:  # Loop over each word and its count
        # Move this word's fence border to the right
        fence += count
        if fence >= dart:   # Check if this word's fence is past the dart
            # Fence is past the dart, so choose this word
            return word

if __name__ == '__main__':
    words = sample(histogram)
    print(words)
        
        