import SquaresSortedArray_977# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(SquaresSortedArray_977.sortedSquares(nums = [-4,-1,0,3,10]), [0,1,9,16,100])
        
    def test_2(self):
        self.assertEqual(SquaresSortedArray_977.sortedSquares([-7,-3,2,3,11]), [4,9,9,49,121])
        

    
if __name__ == '__main__':
    unittest.main()