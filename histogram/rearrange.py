import sys
import python_quote
from random import randint



def rearrange():

    quote = python_quote.random_quote()
    quote_words = quote.split(" ")

    print(quote)

    dictionary_words = {}

    while True:
        random_word = quote_words[randint(0, len(quote_words) -1)]
        if random_word in dictionary_words.keys() and len(dictionary_words) == len(quote_words):
            break
        else:
            dictionary_words[random_word] = random_word

    result = ""

    for key in dictionary_words.keys():
        result += key+" "

    return result


if __name__ == '__main__':
    print(rearrange())

    # print(rearrange())
