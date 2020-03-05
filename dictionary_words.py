import sys
from random import random, randint

file = open("words.txt", "r")

lines = file.readlines()

def dictionary_words():
    words_dict = {}

    for line in lines:
        words = line.rstrip('\n').split()
        for word in words:
            if word in words_dict.keys():
                words_dict[word] += 1
            else:
                words_dict[word] = 1


    return words_dict




if __name__ == '__main__':
    print(dictionary_words())
