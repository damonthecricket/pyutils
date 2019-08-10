
from os import listdir
import file as file
import array as array



def content(path, extensions = []):
	content = []
	for f in listdir(path):
		extension = file.extension_from_path(f)
		if array.is_empty(extensions) or extension in extensions:
			content.append(f)
	content.sort()
	return content