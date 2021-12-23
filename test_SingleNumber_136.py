import SingleNumber_136# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(SingleNumber_136.singleNumber(nums = [2,2,1]),1)
        
    def test_2(self):
        self.assertEqual(SingleNumber_136.singleNumber(nums = [4,1,2,1,2]),4)
        
    def test_3(self):
        self.assertEqual(SingleNumber_136.singleNumber(nums = [1]),1)
    
if __name__ == '__main__':
    unittest.main()