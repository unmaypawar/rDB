import os
import shutil


from helper.join import *
from helper.filter import *
from helper.group import *


def query_data(keywords, database, overall_schema, chunk_size):
	if database == None:
		print('Please select database!')

	else:
		try:
			data = []
			data = keywords[1:]
			data = ' '.join(data)
			data = data[:-1]
			data = data.split('),')
			
			outputs = []
			conditions = []
			operations = []
			for index, i in enumerate(data):
				if index == 0:
					i = i[1:]
					i = i.split(', ')
					outputs = i
				elif index == 1:
					i = i[2:]
					i = i.split(', ')
					conditions = i
				else:
					i = i[2:]
					i = i.split(', ')
					operations = i

			tables = []

			for op in operations:
				if op.startswith('join'):
					op = op.split('= ')
					join(op[1], tables, chunk_size, database)

			if not tables:
				for key in overall_schema:
					if outputs[0] in overall_schema[key]['o']:
						tables.append(key)
						break
			if len(tables) == 1:
				shutil.copy('databases/' + database + '/' + tables[0] + '.csv', 'output.csv')

			order_variables = {'order': 0, 'first': 0, 'skip': 0}
			for c in conditions:
				if c:
					con = c.split('> ')
					if len(con) == 2:
						filtering('greaterthan', con, chunk_size)
					else:
						con = c.split('< ')
						if len(con) == 2:
							filtering('lessthan', con, chunk_size)
						else:
							con = c.split('= ')
							if con[0] in order_variables:
								order_variables[con[0]] = con[1]
							else:
								filtering('equalto', con, chunk_size)
			group_flag = 0
			for op in operations:
				if op.startswith('group'):
					op = op.split('= ')
					agg = outputs[1].split('.')
					group(op[1], agg, chunk_size, order_variables)
					group_flag = 1

			for op in operations:
				if op.startswith('order'):
					op = op.split('= ')
					order_key = op[1]

			if not group_flag:
				with open('output.csv', 'r') as table_file:
					header = table_file.readline().strip().split(',')
					output_dict = {}

					while True:
						chunk = []
						for i in range(chunk_size):
							chunk.append(table_file.readline().strip().split(','))
						if not chunk[0][0]:
							break
						
						for row in chunk:
							if row[0]:
								for column in outputs:
									if column in output_dict:
										output_dict[column].append(row[header.index(column)])
									else:
										output_dict[column] = []
										output_dict[column].append(row[header.index(column)])
								
					output_dict = pd.DataFrame(output_dict)
					output_dict = output_dict.to_dict(orient='records')

					if order_variables['order']:
						if order_variables['order'] == '1':
							output_dict = sorted(output_dict, key=lambda x: x[order_key])
						else:
							output_dict = sorted(output_dict, key=lambda x: x[order_key], reverse=True)

					if order_variables['skip']:
						output_dict = output_dict[int(order_variables['skip']):]

					if order_variables['first']:
						output_dict = output_dict[:int(order_variables['first'])]

					output = pd.DataFrame(output_dict)
					print(output.to_string(index=False))

			os.remove('output.csv')

		except:
			print('Syntax Error!')