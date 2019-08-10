
import unittest
import file



# TestFile

class TestFile(unittest.TestCase):

	def testName(self):
		for m in self._name_mock():
			p = m[0]
			n = m[1]
			name = file.name_from_path(p)
			self.assertEqual(name, n)

	def testExtensions(self):
		for m in self._extension_mock():
			p = m[0]
			e = m[1]
			extension = file.extension_from_path(p)
			self.assertEqual(extension, e)
		

	def _name_mock(self):
		return [
		("unit_tests/data/file.csv", "file.csv")
		]


	def _extension_mock(self):
		return [
		("unit_tests/data/file.csv", "csv")
		]