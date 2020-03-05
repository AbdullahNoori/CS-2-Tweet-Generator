from flask import Flask
from flask import Flask, render_template, request, redirect, url_for

from histogram import histogram, sample
# from Playground import sample_words, get_lines
# define some functions that compose the above modules


app = Flask(__name__)


def get_tweet(num=10):
    sentence = ''
    hist = histogram()

    for i in range(num):
        sentence += sample(hist)+" "

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


if __name__ == '__main__':
    app.run(debug=True)
    # code to run when file is executed
