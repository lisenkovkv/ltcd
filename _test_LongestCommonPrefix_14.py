import LongestCommonPrefix_14   # The code to test
import unittest   # The test framework

class Test_LongestCommonPrefix(unittest.TestCase):
    
    def test_first(self):
        self.assertEqual(LongestCommonPrefix_14.longestCommonPrefix(["flower","flow","flight"]), "fl")

    def test_second(self):
        self.assertEqual(LongestCommonPrefix_14.longestCommonPrefix(["dog","racecar","car"]), "")

    #def test_second(self):
    #    self.assertEqual(LongestCommonPrefix_14.longestCommonPrefix(["dog","racecar","car"]), "")



if __name__ == '__main__':
    unittest.main()