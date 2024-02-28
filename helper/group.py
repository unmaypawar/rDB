import os
import pandas as pd


def group(key, agg, chunk_size, order_variables):
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
					if agg[0] == 'count':
						if row[header.index(key)] in output_dict:
							output_dict[row[header.index(key)]] += 1
						else:
							output_dict[row[header.index(key)]] = 1
					elif agg[0] == 'avg':
						try:
							float(row[header.index(agg[1])])
							if row[header.index(key)] in output_dict:
								output_dict[row[header.index(key)]][0] = ((output_dict[row[header.index(key)]][0] * output_dict[row[header.index(key)]][1]) + float(row[header.index(agg[1])])) / (output_dict[row[header.index(key)]][1] + 1)
								output_dict[row[header.index(key)]][1] = output_dict[row[header.index(key)]][1] + 1
							else:
								output_dict[row[header.index(key)]] = [float(row[header.index(agg[1])]), 1]
						except:
							pass
					elif agg[0] == 'sum':
						try:
							float(row[header.index(agg[1])])
							if row[header.index(key)] in output_dict:
								output_dict[row[header.index(key)]] += float(row[header.index(agg[1])])
							else:
								output_dict[row[header.index(key)]] = float(row[header.index(agg[1])])
						except:
							pass

		if agg[0] == 'avg':
			for i in output_dict:
				output_dict[i] = output_dict[i][0]

		output_rows = [r for r in output_dict]
		if order_variables['order']:
			if order_variables['order'] == '1':
				output_rows = sorted(output_dict, key=lambda x: output_dict[x])
			else:
				output_rows = sorted(output_dict, key=lambda x: output_dict[x], reverse=True)

		if order_variables['skip']:
			output_rows = output_rows[int(order_variables['skip']):]

		if order_variables['first']:
			output_rows = output_rows[:int(order_variables['first'])]

		final_output = {}
		for row in output_rows:
			final_output[row] = output_dict[row]

		output = pd.DataFrame(list(final_output.items()), columns=[key, agg[0]])
		print(output.to_string(index=False))