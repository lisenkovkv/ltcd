import PermutationString_567# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(PermutationString_567.checkInclusion(s1 = "ab", s2 = "eidbaooo"),True)
    
    def test_2(self):
        self.assertEqual(PermutationString_567.checkInclusion(s1 = "ab", s2 = "eidboaoo"),False)

if __name__ == '__main__':
    unittest.main()