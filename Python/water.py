# coding: utf-8
import re
import clipboard


total = 0
print("Type '-' to subtract.\nType 'clear' to start over.\nType 'copy' to copy your total to the clipboard.\nWater (in ints): ")
while True:
	pattern_a=r"[\d]"
	drank = raw_input()
	if re.match(pattern_a, drank):
		total += int(drank)
		print("New total: %d" % total)
	elif drank == "-":
		drank = raw_input("Subtract how much? ")
		total -= int(drank)
		print("New total: %d" % total)
	elif drank.lower() == 'clear':
		total=0
		print("New total: %d" % total)
	elif drank.lower() == 'copy':
		clipboard.set(str(total))
		print("Copied!")
	else:
		print("That's not a number.")
		continue
