import json

def print_authors(*authors_id):
	# printing info about authors by their ids
	myfile = open('parsed_data/data.json', 'r', encoding='utf-8')
	data = json.load(myfile)
	try:
		for id in authors_id:
			print(' \nName:', data[id-1][1][0], '\nBirth:', data[id-1][1][2], 'in', data[id-1][1][3])
	except IndexError:
		print('\nInvalid author\'s id!')

# print_authors_by(1, 99, 4)