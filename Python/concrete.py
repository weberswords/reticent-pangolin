#!/usr/bin/python
#coding: latin-1

'''concrete.py

This program will estimate the cost of building a concrete
enclosure based on input from the user. User will be prompted
to provide height, width, length, size of opening, and the
 thickness of the wall to complete the final enclosure. Output
 will then display entered values as well as estimates for
 concrete, labor, overhead and total of all charges.
it’s going to be done with concrete. which costs $81 per cubic meter. Labor is 60% of the concrete cost, overhead is 20% of the labor cost.
'''

#Ask user for measurements
height = float(input('How tall is your murder dungeon? '))
width = float(input('How wide is your murder dungeon? '))
length = float(input('How deep is your murder dungeon? '))
depth = float(input('How thick would you like the walls of your murder dungeon? '))

#Check to make sure opening height & width do not exceed room measurements
opening_height = float(input('What is height of the opening? '))
while opening_height >= height:
	opening_height = input("Your opening is too tall. Choose a height less than %2f: " % height)

opening_width = float(input('What is the width of the opening? ')) 
while opening_width >= width:
	opening_width = input("Your opening is too wide. Choose a width less than %2f: " % width)

def volume(height, width, depth):
	volume = height * width * depth
	return volume

opening_area = volume(opening_height, opening_width, depth)
wall1 = volume(height, width, depth)
wall2 = volume(length, height, depth)
wall3 = wall1
cubic_meters = ((wall1 + wall2 + wall3)*2) - opening_area
concrete_cost = round(cubic_meters*81, 3)
labor = round(concrete_cost*.6, 2)
overhead = round(labor*.2, 2)
total = concrete_cost + labor + overhead


print('The walls of your {} by {} by {} space measures {} cubic meters.'.format(height, width, length, cubic_meters))
               
print ("Your concrete cost will be: ${}".format(concrete_cost))
print ("Your labor will be: ${}".format(labor))
print ("Your overhead will be: ${}".format(overhead))
print ("The total cost for this project will be: ${}".format(total))



