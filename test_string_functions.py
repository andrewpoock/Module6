from more_functions import string_functions
import unittest

class TestStringMethods(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(string_functions.multiply_string('code', 3), 'codecodecode')


if __name__ == '__main__':
    unittest.main()
