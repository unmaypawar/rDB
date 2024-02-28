import os
import pandas as pd


def filtering(op, con, chunk_size):
	with open('output.csv', 'r') as table_file:
			header = table_file.readline().strip().split(',')
			with open('filtered_output.csv', 'w') as new_table_file:
				new_table_file.write(','.join(header) + '\n')

			while True:
				chunk = []
				to_remove = []
				for i in range(chunk_size):
					chunk.append(table_file.readline().strip().split(','))
				if not chunk[0][0]:
					break
				
				for row in chunk:
					if row[0]:
						if op == 'greaterthan':
							if not row[header.index(con[0])] > con[1]:
								to_remove.append(row)
						elif op == 'lessthan':
							if not row[header.index(con[0])] < con[1]:
								to_remove.append(row)
						else:
							if not row[header.index(con[0])] == con[1]:	
								to_remove.append(row)						 

				for row in to_remove:
					chunk.remove(row)

				with open('filtered_output.csv', 'a') as new_table_file:
					for row in chunk:
						if row[0]:
							new_table_file.write(','.join(row) + '\n')

	os.remove('output.csv')
	os.rename('filtered_output.csv', 'output.csv')