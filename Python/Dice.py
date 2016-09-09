# coding: utf-8
#Created April 2016 with Pythonista for iOS

import random
import sys

def roll():
	diceA = random.randint(1,6)
	diceB = random.randint(1,6)
	roll = raw_input("Roll? y/n ")
	roll = roll.upper()
	
	if roll == "Y":
		print(diceA, diceB)
		
	else:
		print("K. deuces.")
		sys.exit()
	
while True:
	roll()
	

	