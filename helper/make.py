import os
import pickle


def make_database(keywords):
	if len(keywords) != 3:
		print('Syntax Error!')

	elif os.path.exists('databases/' + keywords[2]):
		print('Database already exists!')

	else:
		os.makedirs('databases/' + keywords[2])
		overall_schema_path = 'databases/' + keywords[2] + '/overall_schema.pickle'
		with open(overall_schema_path, 'wb') as pickle_file:
			return


def make_table(keywords, database, overall_schema):
	if len(keywords)<4:
		print('Syntax Error!')

	elif database == None:
		print('Please select database!')

	elif os.path.exists('databases/' + database + '/' + keywords[2] + '.csv'):
		print('Table already exists!')

	else:
		schema = []
		schema = keywords[3:]
		schema = ' '.join(schema)
		schema = schema[1:-1]
		schema = schema.split(',')
		for i in schema:
			schema[schema.index(i)] = i.replace(' ','')

		columns = []
		for i in schema:
			columns.append(i.split('*'))

		constraints = ['pk', 'fk', 'u', 'o']
		for i in columns:
			if len(i)>1:
				if i[1] not in constraints:
					print('Invalid constraint!')
					return

				if i[1] == 'fk':
					if i[2] not in overall_schema:
						print('Table does not exist for foreign key!')
						return
					if i[3] not in overall_schema[i[2]]['pk']:
						print('Column is not primary key of referenced table!')
						return

		file_name = 'databases/' + database + '/' + keywords[2] + '.csv'
		with open(file_name, 'w') as file:
			header = ''
			for column in columns:
				header += column[0] + ','
			header = header[:-1]
			file.write(header + '\n')

		new_schema = {'pk':[], 'fk':[],  'fk_t':[], 'fk_r':[], 'u':[], 'o':[]}
		for i in columns:
			if len(i)>1:
				new_schema[i[1]].append(i[0])
				if i[1] == 'fk':
					new_schema['fk_t'].append(i[2])
					new_schema['fk_r'].append(i[3])
			else:
				new_schema['o'].append(i[0])

		overall_schema[keywords[2]] = new_schema
		overall_schema_path = 'databases/' + database + '/overall_schema.pickle'
		with open(overall_schema_path, 'wb') as pickle_file:
			pickle.dump(overall_schema, pickle_file)