
import unittest
import folder



# TestFolder

class TestFolder(unittest.TestCase):

	def testInstance(self):
		for m in self._content_mock():
			p = m[0]
			c = m[1]
			content = folder.content(p)
			self.assertEqual(content, c)


	def _content_mock(self):
		return [
		("unit_tests/data", ["file.csv"])
		]