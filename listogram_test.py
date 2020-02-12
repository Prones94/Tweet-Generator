#!python

from listogram import Listogram
import unittest
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class ListogramTest(unittest.TestCase):
    fish_txt = ['one', 'fish','two','fish','red','fish','blue', 'fish']
    fish_w_list = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
    fish_w_dict = {'one':1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}

    def test_entries(self):
        listogram = Listogram(self.fish_txt)
        assert len(listogram) == 5
        self.assertCountEqual(listogram, self.fish_w_list)
        dictogram = dict(listogram)
        assert len(dictogram) == 5
        self.assertCountEqual(dictogram, self.fish_w_dict)

    def test_contains(self):
        histogram = Listogram(self.fish_txt)
        for word in self.fish_txt:
            assert wrod in histogram
        for word in ('lush', 'friends'):
            assert word not in histogram
    
    def test_frequency(self):
        histogram = Listogram(self.fish_txt)
        assert histogram.frequency('one') == 1
        assert histogram.frequency('two') == 1
        assert histogram.frequency('red') == 1
        assert histogram.frequency('blue') == 1
        assert histogram.frequency('fish') == 4
        assert histogram.frequency('friends') == 0

    def test_add_count(self):
        histogram = Listogram(self.fish_txt)
        histogram.add_count('two', 2)
        histogram.add_count('blue', 3)
        histogram.add_count('fish', 4)
        histogram.add_count('friends', 5)
        assert histogram.frequency('one') == 1
        assert histogram.frequency('two') == 3
        assert histogram.frequency('red') == 1
        assert histogram.frequency('blue') == 4
        assert histogram.frequency('fish') == 8
        assert histogram.frequency('friends') == 5
        assert histogram.types == 6
        assert histogram.tokens == 8 + 14

    def test_tokens(self):
        histogram = Listogram(self.fish_txt)
        assert len(self.fish_txt) == 8
        assert histogram.tokens == 8
        for word in self.fish_txt:
            histogram.add_count(word)
        assert histogram.tokens == 8 + 8

    def test_types(self):
        histogram = Listogram(self.fish_txt)
        assert len(set(self.fish_txt)) == 5
        assert histogram.types == 5
        for word in self.fish_txt:
            histogram.add_count(word)
        assert histogram.types == 5

    def test_sample(self):
        histogram = Listogram(self.fish_txt)
        sample_list = [histogram.sample() for _ in range(10000)]
        sample_histo = Listogram(sample_list)
        for word, count in histogram:
            observed_freq = count / histogram.tokens
            sampled = sample_histo.frequency(word)
            frequency_sample = sampled / sample_histo.tokens
            low_range = observed_freq * 0.9
            up_range = observed_freq * 1.1
            assert low_range <= frequency_sample <= up_range

if __name__ == '__main__':
    unittest.main()