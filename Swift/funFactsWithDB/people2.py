#!/usr/bin/env python

from getpass import getpass
import sys
from collections import OrderedDict

from peewee import *
from playhouse.sqlcipher_ext import SqlCipherDatabase

db = SqlCipherDatabase('None')

class Person(Model):
	lastName = CharField()
	firstName = CharField()
	# birthday = DateField()
	# is_relative = BooleanField()

	class Meta:
		database = db

def initialize(passphrase):
	db.init('people.db', passphrase=passphrase, kdf_iter=64000)
	Person.create_table(fail_silently=True)

def menu_loop():
	choice = None
	while choice != 'q':
		for key, value in menu.items():
			print('%s) %s' % (key, value.__doc__))
		choice = raw_input('Action: ').lower().strip()
		if choice in menu:
			menu[choice]()

def add_person():
	"""Add a new person"""
	print('Enter first and last name. Press ctrl+d when finished.')
	data = sys.stdin.read().strip().split(' ')

	if data and raw_input('Save person? [Yn] ') != 'n':
		Person.create(firstName=data[0], lastName=data[1])
		print('New person added!')

def view_people(search_people=None):
	"""View people"""
	query = Person.select().order_by(Person.lastName.desc())
	if search_people:
		query = query.where(Person.lastName.contains(search_people))

	for person in query:
		lastname = person.lastName
		firstname = person.firstName
		print('%s, %s' % (lastname, firstname))
		print('=' * 30)
		print('n) next person')
		print('q) return to main menu')
		action = raw_input('Choice? (Nq) ').lower().strip() 
		if action == 'q':
			break

def search_people():
	"""Search people"""
	view_people(raw_input('Search query: '))

menu = OrderedDict([
	('a', add_person),
	('v', view_people),
	('s', search_people),
])

if __name__ == '__main__':
	passphrase = getpass('Enter password:')

	if not passphrase:
		sys.stderr.write('Passphrase require to access list.\n')
		sys.stderr.flush()
		sys.exit(1)

	initialize(passphrase)
	menu_loop()
