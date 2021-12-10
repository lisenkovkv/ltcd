import  SortingSentence_1859 # The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(SortingSentence_1859.sortSentence(s = "is2 sentence4 This1 a3"), "This is a sentence")
    
    def test_2(self):
        self.assertEqual(SortingSentence_1859.sortSentence(s = "Myself2 Me1 I4 and3"), "Me Myself and I")
    
if __name__ == '__main__':
    unittest.main()