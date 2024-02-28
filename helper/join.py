import os
import pandas as pd 
import csv


def join(op_input, tables, chunk_size, database):
	op_input = op_input.split('=')
	join_columns = []
	for i in op_input:
		tables.append(i.split('.')[1])
		join_columns.append(i.split('.')[0])

	for table in tables:
		file_path = 'databases/' + database + '/' + table + '.csv'
		output_path =  table + '_sorted.csv'
		sort_large_csv(file_path, output_path, chunk_size)

	file1_path = tables[0] + '_sorted.csv'
	file2_path = tables[1] + '_sorted.csv'
	data1 = read_csv(file1_path, 'id')
	data2 = read_csv(file2_path, 'id')

	result = join_dicts(data1, data2, 'id')
	header = result[0].keys()
	output_path = 'output.csv'
	with open(output_path, 'w', newline='') as output_file:
	    writer = csv.DictWriter(output_file, fieldnames=header)
	    writer.writeheader()
	    writer.writerows(result)

	os.remove(file1_path)
	os.remove(file2_path)


def sort_large_csv(input_file, output_file, chunk_size):
    chunks = pd.read_csv(input_file, chunksize=chunk_size)

    sorted_chunks = []
    for chunk in chunks:
        sorted_chunk = chunk.sort_values(by=['id'], ascending=True)
        sorted_chunks.append(sorted_chunk)

    sorted_data = pd.concat(sorted_chunks)

    sorted_data.to_csv(output_file, index=False)


def read_csv(file_path, key_column):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = row[key_column]
            data[key] = row
    return data


def join_dicts(dict1, dict2, key):
    result = []
    for common_key in set(dict1.keys()) & set(dict2.keys()):
        result.append({**dict1[common_key], **dict2[common_key]})
    return result