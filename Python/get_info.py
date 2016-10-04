#!/usr/bin/python
#encoding='utf-8'

'''
Created by: Stephanie Weber
Created on: September 12, 2016
'''

import calendar, csv, operator

from datetime import date

#find data where user started before sept 6, 2010
target_date = date(2010, 9, 6)
date_timestamp = calendar.timegm(target_date.timetuple())

#create header row
def create_header(writer, reader):
	fields = reader.next()
	writer.writerow(fields)

#open file
with open('TSE_sample_data.csv') as data:
	extracted_data = open('extracted_data.csv', 'w')
	file_writer = csv.writer(extracted_data)
	reader = csv.reader(data)
	create_header(file_writer, reader)
	for row in reader:
		test_date = float(row[13])
		if test_date < date_timestamp:
			file_writer.writerow(row)
		else:
			pass
extracted_data.close()

# order values from words column in ascending order by start date
with open('extracted_data.csv') as extracted_data:
	sorted_data = open('sorted_data.csv', 'w')
	sorted_writer = csv.writer(sorted_data)
	extracted_data_reader = csv.reader(extracted_data)
	create_header(sorted_writer, extracted_data_reader)
	sort = sorted(extracted_data_reader, key=operator.itemgetter(13))
	for line in sort:
		sorted_writer.writerow(line)
sorted_data.close()




