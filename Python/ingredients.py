#!/usr/bin/python
#encoding='utf-8'

class Ingredient(object):
	quantity
	unit
	item

with open('ingredients.txt') as ingredients:
	for line in ingredients:
		line_list = line.split()
		quantity = line_list[0]
		if line_list[1] == 

