import os
import pickle


def shift_database(database, keywords, overall_schema):
	if len(keywords) != 2:
		print('Syntax Error!')

	else:
		databases = os.listdir('databases')
		if not keywords[1] in databases:
			print('Database does not exist')
		else:
			database[0] = keywords[1]
			overall_schema = {}
			try:
				overall_schema_path = 'databases/' + database[0] + '/overall_schema.pickle'
				with open(overall_schema_path, 'rb') as pickle_file:
					overall_schema = pickle.load(pickle_file)
			except:
				pass

	return overall_schema