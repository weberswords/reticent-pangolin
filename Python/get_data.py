#!/usr/bin/python
#encoding='utf-8'

'''
Created by: Stephanie Weber
Created on: October 3, 2016
'''

import sys, csv, re
mydict={}
with open(sys.argv[1]) as data:
	for line in data:
		snp_id, pt_id = (
			item.strip() for item in line.split(' ', 1))
		pt_id = pt_id.split(',')
		
		for item in pt_id:
			if item in mydict.keys():
				mydict[item].append(snp_id)
			else:
				mydict.update({item:[snp_id]})
	
w = open('new_data.txt', 'w')
for key, val in mydict.items():
 	val = ','.join(val)
 	w.writelines("{} {}\n".format(key, val))
