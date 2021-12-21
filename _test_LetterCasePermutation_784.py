import LetterCasePermutation_784# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(LetterCasePermutation_784.letterCasePermutation(s = "a1b2"),["a1b2","a1B2","A1b2","A1B2"].sort())

    def test_2(self):
        self.assertEqual(LetterCasePermutation_784.letterCasePermutation(s = "3z4"),["3z4","3Z4"].sort())
        
    def test_3(self):
        self.assertEqual(LetterCasePermutation_784.letterCasePermutation(s = "12345"),["12345"].sort())
        
    def test_4(self):
        self.assertEqual(LetterCasePermutation_784.letterCasePermutation(s = "0"),["0"].sort())

    
if __name__ == '__main__':
    unittest.main()