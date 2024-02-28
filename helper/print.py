import os 
import pandas as pd


def print_data(keywords, database, overall_schema, chunk_size):
	if database == None:
		print('Please select database!')
	
	elif keywords[1] != 'in' or keywords[2] not in overall_schema:
		print('Syntax Error!')

	else:
		data = []
		data = keywords[3:]
		data = ' '.join(data)
		data = data[1:-1]
		data = data.split(',')
		for i in data:
			data[data.index(i)] = i.replace(' ','')

		table_path = 'databases/' + database + '/' + keywords[2] + '.csv'
		with open(table_path, 'r') as table_file:
			header = table_file.readline()
		header = header.strip().split(',')

		columns = data

		for column in columns:
			if column not in header:
				print('Attribute does not exist!')
				return

		column_index = []
		for key in columns:
			column_index.append(header.index(key))

		with open(table_path, 'r') as table_file:
			table_file.readline()
			flag = 0
			while True:
				chunk = {}
				for i in columns:
					chunk[i] = []

				for i in range(chunk_size):
					row = table_file.readline().strip().split(',')
					for k,j in enumerate(columns):
						if row[0] == '':
							flag = 1
							break
						else:
							chunk[j].append(row[column_index[k]])

					if flag == 1:
						break

				df = pd.DataFrame(chunk)
				if not df.empty:
					print(df.to_string(index=False, header=False))	

				if flag == 1:
					break			