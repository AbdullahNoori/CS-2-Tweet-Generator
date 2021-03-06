#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
from random import randint


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)


    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        # if word in self:
        for pair in self:
            if pair[0] == word:
                pair[1] += count
                self.tokens += count
                self.types = self.__type__()
                return

        self.tokens += count
        pair = [word, count]
        self.append(pair)
        self.types = self.__type__()



    def __type__(self):
        return len(self)


    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        # print("Looking for ", word)
        if not self.__contains__(word):
            return 0 #return 0 count if word is not in list
        else: # if it exist
            index = self.index_of(word) #must use self.
            # print(f"{self[index][0]} exist in {self[index][1]}")
            return self[index][1] #list[index][0] has the word, and list[index][1] has the count

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        for word_list in self:
            if word == word_list[0]:
                return True
        return False

    def index_of(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        index = 0
        for word_list in self:
            if word_list[0] == target: #if we find the word, then return index
                return index
            index += 1
        return index


    def print_histogram(word_list):
        print('word list: {}'.format(word_list))
        # Create a listogram and display its contents
        histogram = Listogram(word_list)
        print('listogram: {}'.format(histogram))
        print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
        for word in word_list[-2:]:
            freq = histogram.frequency(word)
            print('{!r} occurs {} times'.format(word, freq))
        print()


    def main():
        import sys
        arguments = sys.argv[1:]  # Exclude script name in first argument
        if len(arguments) >= 1:
            # Test histogram on given arguments
            print_histogram(arguments)
        else:
            # Test histogram on letters in a word
            word = 'abracadabra'
            print_histogram(list(word))
            # Test histogram on words in a classic book title
            fish_text = 'one fish two fish red fish blue fish'
            print_histogram(fish_text.split())
            # Test histogram on words in a long repetitive sentence
            woodchuck_text = ('how much wood would a wood chuck chuck'
                              ' if a wood chuck could chuck wood')
            print_histogram(woodchuck_text.split())

if __name__ == '__main__':
    main()
