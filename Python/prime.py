#prime - Created December 2015

import sys

if len(sys.argv) < 2:
	print("usage: prime.py [positive integer]")
	sys.exit()

if len(sys.argv) > 2:
	print("Only one argument at a time please.")
	quit()

input = int(sys.argv[1])

def prime(input):
	for number in range(2,input/2):
		if input%number == 0:
			# print("%d is not prime." % input)
			return False
	print("%d is totes prime." % input)
	return True

while not prime(input):
	input += 1
