import sys
import scrabble

from flask import Flask
app = Flask(__name__)


@app.route('/<racktext>')
def index(racktext):
	rack = list(racktext.lower())
	valid_words = []
	return_values = ""

	for word in scrabble.wordlist:
		if valid_word(word, rack):
			score = compute_score(word)
			valid_words.append([score, word])

	valid_words.sort()
	for play in valid_words:
		score = play [0]
		word = play [1]
		return_values = return_values + word + ": " + str(score) + "<br>"
	
	return "Your rack is {0}.<br>Your options are:<br>{1}".format(racktext, return_values)


def valid_word(word, rack):
	available_letters = rack[:]
	for letter in word:
		if letter not in available_letters:
			return False
		available_letters.remove(letter)
	return True

def compute_score(word):
	score = 0
	for letter in word:
		score = score + scrabble.scores[letter]
	return score


if __name__ == '__main__':
    app.debug = False 
    app.run(host='0.0.0.0')
