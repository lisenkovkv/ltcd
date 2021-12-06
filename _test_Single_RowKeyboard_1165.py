import Single_RowKeyboard_1165 # The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(Single_RowKeyboard_1165.calculateTime(keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"), 4)
    
    def test_2(self):
        self.assertEqual(Single_RowKeyboard_1165.calculateTime(keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"), 73)

if __name__ == '__main__':
    unittest.main()