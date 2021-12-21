import HouseRobber_198# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(HouseRobber_198.rob(nums = [1,2,3,1]),4)
    
    def test_2(self):
        self.assertEqual(HouseRobber_198.rob(nums = [2,7,9,3,1]),12)

    
if __name__ == '__main__':
    unittest.main()