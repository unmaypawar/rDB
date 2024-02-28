import os


def list_databases(keywords):
	if len(keywords) != 2:
		print('Syntax Error!')

	else:
		databases = os.listdir('databases')
		for database in databases:
			if database != '.DS_Store':
				print(database)


def list_tables(keywords, database, overall_schema):
	if len(keywords) != 2:
		print('Syntax Error!')

	elif database == None:
		print('Please select database!')

	else:
		for table in overall_schema:
			print(table)