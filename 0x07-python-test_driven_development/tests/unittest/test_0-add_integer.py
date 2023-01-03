import unittest
from 0-add_integer import add_integer
class Testadd_integer(unittest.TestCase):
    add_integer = __import__('0-add_integer').add_integer

    def test_add(self):
        result = add_integer(12, 7)
        self.assertEqual(result, 19)
