import os


def modify_data(keywords, database, overall_schema, chunk_size):
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
			column_value_dict[i] = column_value_dict[i][1:-1]

		table_path = 'databases/' + database + '/' + keywords[2] + '.csv'
		with open(table_path, 'r') as table_file:
			header = table_file.readline()
		header = header.strip().split(',')

		for column in column_value_dict:
			if column not in header:
				print('Attribute does not exist!')
				return
		
		column_index = []
		for key in column_value_dict:
			column_index.append(header.index(key))

		new_table_path = 'databases/' + database + '/' + keywords[2] +'_copy.csv'
		with open(new_table_path, 'a') as new_table_file:
			new_table_file.write(','.join(header) + '\n')
		
		with open(table_path, 'r') as table_file:
			table_file.readline()
			while True:
				chunk = []
				for i in range(chunk_size):
					chunk.append(table_file.readline().strip().split(','))
				if not chunk[0][0]:
					break

				for row in chunk:
					try:
						if row[column_index[0]] == column_value_dict[header[column_index[0]]]:
							for index in column_index:
								chunk[chunk.index(row)][chunk[chunk.index(row)].index(row[index])] = column_value_dict[header[index]]
					except:
						pass
						
				with open(new_table_path, 'a') as new_table_file:
					for row in chunk:
						if row[0]:
							new_table_file.write(','.join(row) + '\n')

		os.remove(table_path)
		os.rename(new_table_path, table_path)