


def last(array):
	if len(array) > 0:
		return array[len(array) - 1]
	else:
		return None


def is_empty(array):
	return len(array) == 0


def is_elements(array):
	return is_empty(array) is False