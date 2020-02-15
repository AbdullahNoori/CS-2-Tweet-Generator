import random
from random import randint
import sys
import dictionary_words

some_file = "words.txt"
some_lines = open(some_file, "r")

histograms = {"one": 2,
            "fish": 4, "red": 2, "blue": 2
        }

def histogram(histograms):
    for word in some_lines:
        word = word.rstrip()

        if word in histograms:
            histograms[word] += 1
        else:
            histograms[word] = 1
    random_index = randint(0, len(histograms)-2)
    print(histoogram, random_index)

def unique_words():
    count = 0
    for word in histograms:
        #check if word is unique, only seen once
        if histograms[word] == 1:
            count += 1
        else:
            return('error')
    return(count)

def frequency():
    for word in histograms:
        print(f'the word {word} is repeated {histograms[word]} times.')



if __name__ == '__main__':
    print(histogram(histograms))
    print(unique_words())
    print(frequency()
