import  CheckTwoStringArraysEquivalent_1662 # The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(CheckTwoStringArraysEquivalent_1662.arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]), True)
    
    def test_2(self):
        self.assertEqual(CheckTwoStringArraysEquivalent_1662.arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"]), False)
        
    def test_3(self):
        self.assertEqual(CheckTwoStringArraysEquivalent_1662.arrayStringsAreEqual(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]), True)

    
if __name__ == '__main__':
    unittest.main()