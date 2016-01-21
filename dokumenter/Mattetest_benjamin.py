import unittest

class Testadd(unittest.Testcase):
    def setup (self):
        pass
    def test_numbers_8_9(self):
        self.assertEqual(multiply(8,9),72)
        
    
if __name__ == '__main__':
    unittest.main()