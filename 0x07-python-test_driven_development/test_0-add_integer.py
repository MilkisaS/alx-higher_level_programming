import unittest
import 0-add_integer

class TestAdd_Integer(unittest,TestCase):
	def test_add_integer(self):
	    result = add_integer(22, 3)
	    self.assertEqual(result, 25)
