import ReverseWordsString_557# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(ReverseWordsString_557.reverseWords(s = "Let's take LeetCode contest"),"s'teL ekat edoCteeL tsetnoc")

    def test_2(self):
        self.assertEqual(ReverseWordsString_557.reverseWords(s = "God Ding"),"doG gniD")

        

    
if __name__ == '__main__':
    unittest.main()