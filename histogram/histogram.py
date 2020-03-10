import random
from random import randint
import sys
# import dictionary_words

some_file = "words.txt"
some_lines = open(some_file, "r")

histograms = {"one": 2,
            "fish": 4, "red": 2, "blue": 2
        }

def histogram():
    file = open("words.txt", "r")
    lines = file.readlines()

    histogram = {}

    for line in lines:
        words = line.rstrip('\n').split()
        for word in words:
            if word in histogram.keys():
                histogram[word] += 1
            else:
                histogram[word] = 1

    return histogram

def unique_words():
    count = 0
    for word in histograms:
        #check if word is unique, only seen once
        if histograms[word] == 1:
            count += 1
        else:
            return('error')
    return(count)



def sample(histogram):
    tokens = 0
    for k,v in histogram.items():
        tokens += v
    dart = randint(1, tokens)
    fence = 0
    for word,count in histogram.items():
        fence += count
        if fence >= dart:
            return word



def frequency():
    for word in histograms:
        print(f'the word {word} is repeated {histograms[word]} times.')



if __name__ == '__main__':
    print(histogram(histograms))
    print(unique_words())
    print(frequency())
