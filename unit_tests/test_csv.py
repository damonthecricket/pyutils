
import unittest
import csv_util



# TestCSV

class TestCSV(unittest.TestCase):

	def testLoad(self):
		for path in self._mock():
			c = csv_util.load_dictionary(path)

			self.assertTrue(len(c) != 0)


		for path in self._mock():
			c = csv_util.load(path)

			self.assertTrue(len(c) != 0)


	def _mock(self):
		return [
		"unit_tests/data/file.csv"
		]
		