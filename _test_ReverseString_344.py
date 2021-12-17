import ReverseString_344# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(ReverseString_344.reverseString(s = ["h","e","l","l","o"]),["o","l","l","e","h"])
        
    def test_2(self):
        self.assertEqual(ReverseString_344.reverseString(s = ["H","a","n","n","a","h"]),["h","a","n","n","a","H"])
        

    
if __name__ == '__main__':
    unittest.main()