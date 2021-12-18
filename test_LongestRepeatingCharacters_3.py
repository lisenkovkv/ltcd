import LongestRepeatingCharacters_3# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(LongestRepeatingCharacters_3.lengthOfLongestSubstring(s = "abcabcbb"),3)
    
    def test_2(self):
        self.assertEqual(LongestRepeatingCharacters_3.lengthOfLongestSubstring(s = "bbbbb"),1)
        
    def test_3(self):
        self.assertEqual(LongestRepeatingCharacters_3.lengthOfLongestSubstring(s = "pwwkew"),3)
  
if __name__ == '__main__':
    unittest.main()