import  SplitStringBalancedStrings_1221 # The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(SplitStringBalancedStrings_1221.balancedStringSplit(s = "RLRRLLRLRL"), 4)
    
    def test_2(self):
        self.assertEqual(SplitStringBalancedStrings_1221.balancedStringSplit(s = "RLLLLRRRLR"), 3)
        
    def test_3(self):
        self.assertEqual(SplitStringBalancedStrings_1221.balancedStringSplit(s = "LLLLRRRR"), 1)
    
    def test_4(self):
        self.assertEqual(SplitStringBalancedStrings_1221.balancedStringSplit(s = "RLRRRLLRLL"), 2)
    
if __name__ == '__main__':
    unittest.main()