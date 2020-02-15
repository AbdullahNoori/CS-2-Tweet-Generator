# import random 

# colors = ['red', 'yellow', 'green', 'blue']

# wTotal = sum(weights.values())

# results = {}


# for i in range(10000):
#     wRndNr = random.randint(0, wTotal -1)

# def sample(words):
#     index = random.randint(0, len(words)-1)
#     return words[index]

# print(sample(colors))


histogram = ('one fish', 'two fish', 'red fish', 'blue fish')

def sample(histogram):
    random_index = randint(0, len(histogram)-1)