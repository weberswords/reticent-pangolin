''' 
Created December 2015

fibonacci
all numbers less than 4,000,000 in fib seq
if even add to total
'''

current = 2
previous = 1
total = 2

while previous + current <= 4000000:
	next = previous + current
	if next%2 == 0:
		total += next
	previous = current
	current = next
	print(current)
print(total)
