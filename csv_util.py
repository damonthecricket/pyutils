
import csv



def load_dictionary(path):
	c = []
	with open(path, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for dictionary in reader:
			c.append(dictionary)
	return c



def load(path, newline = '', delimiter = ' ', quotechar = '|'):
	c = []
	with open(path, newline = newline) as csvfile:
		reader = csv.reader(csvfile, delimiter = delimiter, quotechar = quotechar)
		for row in reader:
			c.append(row)
	return c