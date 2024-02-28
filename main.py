import os
import pickle


from helper.make import *
from helper.shift import *
from helper.list import *
from helper.put import *
from helper.modify import *
from helper.remove import *
from helper.print import *
from helper.query import *


cmd = 'start'
database = []
database.append(None)
overall_schema = {}
chunk_size = 500
import_flag = 0
import_cmd = []


while cmd != 'stop.':
	if import_flag == 0:
		cmd = input('rDB > ')

	else:
		cmd = import_cmd[0].strip()
		import_cmd = import_cmd[1:]

		if not import_cmd:
			import_flag = 0

	while cmd[-1] != '.':
		cmd += ' ' + input('    > ')
	keywords = cmd.split(' ')
	keywords[-1] = keywords[-1][:-1]


	if keywords[0] == 'make' and keywords[1] == 'database':
		make_database(keywords)


	elif keywords[0] == 'make' and keywords[1] == 'table':
		make_table(keywords, database[0], overall_schema)


	elif keywords[0] == 'shift':
		overall_schema = shift_database(database, keywords, overall_schema)	


	elif keywords[0] == 'list'and keywords[1] == 'databases':
		list_databases(keywords)


	elif keywords[0] == 'list' and keywords[1] == 'tables':
		list_tables(keywords, database[0], overall_schema)


	elif keywords[0] == 'put':
		put_data(keywords, database[0], overall_schema, chunk_size)


	elif keywords[0] == 'modify':
		modify_data(keywords, database[0], overall_schema, chunk_size)


	elif keywords[0] == 'remove':
		remove_data(keywords, database[0], overall_schema, chunk_size)


	elif keywords[0] == 'print':
		print_data(keywords, database[0], overall_schema, chunk_size)


	elif keywords[0] == 'import' and os.path.exists(keywords[1]):
		import_flag = 1
		with open(keywords[1], 'r') as file:
			import_cmd = file.readlines()


	elif keywords[0] == 'query':
		query_data(keywords, database[0], overall_schema, chunk_size)