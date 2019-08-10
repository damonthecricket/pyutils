
from os import listdir

try:
	from . import file
	from . import array
except:
	import file
	import array



def content(path, extensions = []):
	content = []
	for f in listdir(path):
		extension = file.extension_from_path(f)
		if array.is_empty(extensions) or extension in extensions:
			content.append(f)
	content.sort()
	return content