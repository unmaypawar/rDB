import os


def put_data(keywords, database, overall_schema, chunk_size):
	if database == None:
		print('Please select database!')

	elif keywords[1] != 'in' or keywords[2] not in overall_schema:
		print('Syntax Error!')

	else:
		data = []
		data = keywords[3:]
		data = ' '.join(data)
		data = data[1:-1]
		
		column_value_pairs = data.split(', ')
		column_value_dict = dict(pair.split('=') for pair in column_value_pairs)
		for i in column_value_dict:
			column_value_dict[i] = column_value_dict[i][1:]

		table_path = 'databases/' + database + '/' + keywords[2] + '.csv'
		with open(table_path, 'r') as table_file:
			header = table_file.readline()
		header = header.strip().split(',')
		
		for column in column_value_dict:
			if column not in header:
				print('Attribute does not exist!')
				return

		primary_index_dict = {}
		for key in overall_schema[keywords[2]]['pk']:
			primary_index_dict[key] = header.index(key)
		if primary_index_dict:
			with open(table_path, 'r') as table_file:
				table_file.readline()
				while True:
					chunk = []
					for i in range(chunk_size):
						chunk.append(table_file.readline().strip().split(','))
					if not chunk[0][0]:
						break
					for row in chunk:
						for key in primary_index_dict:
							if row[primary_index_dict[key]] == column_value_dict[key]:
								print('Primary key constraint violated!')
								return

		value = ','.join(column_value_dict.values())
		with open(table_path, 'a') as table_file:
			table_file.write(value + '\n')