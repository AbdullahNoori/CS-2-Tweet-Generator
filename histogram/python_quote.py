import random

quotes = ("It's just a flesh wound.",
          "He's not the Messiah.",
          "THIS IS AN EX-PARROT!!",
          "He's a very naughty boy!",)

def random_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_quote()
    print(quote)
