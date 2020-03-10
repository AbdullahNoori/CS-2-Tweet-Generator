# from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
# from histogram import histogram, sample
# from Playground import sample_words, get_lines
# define some functions that compose the above modules
import os
import random
from histogram.histogram import Histogram
from markov import MarkovChain
from histogram.sample import sample, words_list
from histogram.dictogram import Dictogram

app = Flask(__name__)


def get_tweet(num=10):
    sentence = ''
    hist = histogram()

    for i in range(num):
        sentence += sample(hist)+" "

    return sentence

def markov(num=0):

    list_of_words = words_list()

    markovChain = MarkovChain(list_of_words)

    sentence = markovChain.walk(10)

    return sentence

# default 10 words returned to user
@app.route('/')
def words_generator():
    sentence = get_tweet()
    return render_template('index.html', sentence=sentence)

# custom route to return n words
@app.route('/<num>')
def words_generator_limit(num):
    sentence = get_tweet(int(num))
    return render_template('index.html', sentence=sentence)
def markov(num=0):

    list_of_words = words_list()

    markovChain = MarkovChain(list_of_words)

    sentence = markovChain.walk(10)

    return sentence


# helper function to get number
def check_number(num):
    try:
        count = int(num)
        return count
    except ValueError as verr:
        print("Invalid number enter a number")
        return False
    except Exception as ex:
        print(ex)
        return False

# markov default 10 words
@app.route('/markov')
@app.route('/')
def home_route():
    tweet = markov(10)
    navBar_message = markov(5)
    return render_template('index.html', tweet=tweet, navBar_message=navBar_message)

# markov get num words
@app.route('/markov/<num>')
@app.route('/<num>')
def dict_home_route(num):
    count = check_number(num)
    tweet = markov(count)
    navBar_message = markov(10)
    return render_template('index.html', tweet=tweet, navBar_message=navBar_message)


#dictogram default 10 words
@app.route('/dictogram')
def dict_limit_words_route():
    tweet = get_sentence_from_histogram(10)
    navBar_message = get_sentence_from_histogram(random.randint(0, 10))
    return render_template('index.html', tweet=tweet[0], navBar_message=navBar_message)


# get num of words in a tweets
@app.route('/dictogram/<num>')
def limit_words_route(num):
    count = check_number(num)
    tweet = get_sentence_from_histogram(count)
    return render_template('index.html', tweet=tweet[0], navBar_message=tweet[1])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
