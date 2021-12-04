import JewelsandStones_771  # The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_first(self):
        self.assertEqual(JewelsandStones_771.numJewelsInStones("aA","aAAbbbb"), 3)
        
    def test_second(self):
        self.assertEqual(JewelsandStones_771.numJewelsInStones("z","ZZ"), 0)

if __name__ == '__main__':
    unittest.main()