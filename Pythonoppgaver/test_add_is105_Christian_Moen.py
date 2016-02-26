import unittest
from math2_Christian_Moen import add

class TestAdd(unittest.TestCase):
    def setUp(self):
        pass
    def test_numbers_5_2(self):
        self.assertEqual(add(5,2), 7)
    def test_numbers_2_2(self):
        self.assertEqual(add(2,2), 4)
    def test_numbers_5_5(self):
        self.assertEqual(add(5,5), 10)

if __name__ == '__main__':
    unittest.main()
