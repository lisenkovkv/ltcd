import BinarySearch_704 # The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(BinarySearch_704.search(nums = [-1,0,3,5,9,12], target = 9), 4)
    
    def test_2(self):
        self.assertEqual(BinarySearch_704.search(nums = [-1,0,3,5,9,12], target = 2), -1)

    
if __name__ == '__main__':
    unittest.main()