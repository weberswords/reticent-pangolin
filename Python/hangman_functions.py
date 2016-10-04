#!/usr/bin/python
#encoding='utf-8'

'''
Created on: September 11, 2016
Created by: Webs
'''
class Game(object):
	def __init__(self, wrong_guesses_remaining=5, guess_list=[]):
		self.wrong_guesses_remaining = wrong_guesses_remaining
		self.guess_list = guess_list

	def get_word(self, word=raw_input("Choose your word: "), 
						guessing_word=list("_"*len(word))):
		self.list(word) = word
		self.guessing_word = guessing_word

	def print_word(guessing_word):
		print(" ".join(guessing_word))

	def have_turns_left(wrong_guesses_remaining, word):
		if wrong_guesses_remaining > 0:
			print("Guess again!")
			print("You have %d turns remaining." % (wrong_guesses_remaining))
			print("Letters guessed: %s" % guess_list)
		else:	
			print("Sorry! You lost!")
			print("The word was: %s" % "".join(word))

	def check_for_win(guess_list, word):
		if set(guess_list).intersection(word) == set(word):
			print("You win!")
			print("The word was: %s" % "".join(word))
			return False
		else:
			return True

	def find_letter_in_word(curr_guess, guess_list, guessing_word, word):
		for letter in word:
			n=0
			while n < len(word):
				if word[n] == curr_guess:
					guessing_word[n] = curr_guess
					n+=1
					check_for_win(guess_list, word)
				else:
					n+=1

	def check_guess(curr_guess, guessing_word, guess_list, word, wrong_guesses_remaining):
		#did you guess that
		if curr_guess in guess_list:
			print("You already tried that.")
			print("Letters guessed: %s" % guess_list)
			print_word(guessing_word)
		#right
		elif curr_guess in word:
			print("Correct!")
			guess_list.append(curr_guess) #add that to the guess list
			find_letter_in_word(curr_guess, guess_list, guessing_word, word)
			print("Letters guessed: %s" % guess_list)
		#wrong
		else:
			print("Nope!")
			guess_list.append(curr_guess)
			wrong_guesses_remaining -= 1
			have_turns_left(wrong_guesses_remaining, word)

	def ask_and_check(guessing_word, guess_list, word, wrong_guesses_remaining):
		#get a letter
		curr_guess = raw_input("Guess a letter: ")
		#check guess
		check_guess(curr_guess, guessing_word, guess_list, word, wrong_guesses_remaining)


