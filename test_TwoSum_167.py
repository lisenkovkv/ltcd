import TwoSum_167# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(TwoSum_167.twoSum(numbers = [2,7,11,15], target = 9),[1,2])
        
    def test_2(self):
        self.assertEqual(TwoSum_167.twoSum(numbers = [2,3,4], target = 6),[1,3])
        
    def test_3(self):
        self.assertEqual(TwoSum_167.twoSum(numbers = [-1,0], target = -1),[1,2])
        

    
if __name__ == '__main__':
    unittest.main()