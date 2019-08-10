
import unittest
import array



# TestArray

class TestArray(unittest.TestCase):

	def testLast(self):
		for m in self._last_mock():
			a = m[0]
			l = m[1]

			last = array.last(a)

			self.assertEqual(last, l)


	def testEmpty(self):
		for m in self._empty_mock():
			a = m[0]
			i_e = m[1]

			is_empty = array.is_empty(a)

			self.assertEqual(is_empty, i_e)


	def testIsElements(self):
		for m in self._is_elements_mock():
			a = m[0]
			i_e = m[1]

			is_elements = array.is_elements(a)

			self.assertEqual(is_elements, i_e)


	def _last_mock(self):
		return [
		([1], 1),
		([1, 2], 2),
		([1, 2, 3], 3),
		([1, 2, 3, 4], 4),
		([1, 2, 3, 4, 5], 5),
		([1, 2, 3, 4, 5, 6], 6)
		]


	def _empty_mock(self):
		return [
		([1, 2, 3], False),
		([1, 2], False),
		([1], False),
		([], True)
		]


	def _is_elements_mock(self):
		return [
		([1, 2, 3], True),
		([1, 2], True),
		([1], True),
		([], False)
		]
