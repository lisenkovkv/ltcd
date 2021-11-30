import RemoveVowelsfromaString_1119  # The code to test
import unittest   # The test framework

class Test_LongestCommonPrefix(unittest.TestCase):
    
    def test_first(self):
        self.assertEqual(RemoveVowelsfromaString_1119.removeVowels("leetcodeisacommunityforcoders"), "ltcdscmmntyfrcdrs")

    def test_second(self):
        self.assertEqual(RemoveVowelsfromaString_1119.removeVowels("aeiou"), "")

    #def test_second(self):
    #    self.assertEqual(LongestCommonPrefix_14.longestCommonPrefix(["dog","racecar","car"]), "")



if __name__ == '__main__':
    unittest.main()