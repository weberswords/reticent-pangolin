'''
Created December 2015
make a list of numbers 1-100
print number
if a number is a multiple of 3 type fizz
if a number is a multiple of 5 type buzz
if it's both type fizzbuzz
'''

for number in range(1,101):
	print number
	if number%3 == 0:
		print('fizz')
	if number%5 == 0:
		print('buzz')
