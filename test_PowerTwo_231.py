import PowerTwo_231# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(PowerTwo_231.isPowerOfTwo(n = 1),True)

    def test_2(self):
        self.assertEqual(PowerTwo_231.isPowerOfTwo(n = 16),True)

    def test_3(self):
        self.assertEqual(PowerTwo_231.isPowerOfTwo(n = 3),False)
    
if __name__ == '__main__':
    unittest.main()