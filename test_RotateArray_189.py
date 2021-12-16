import RotateArray_189# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(RotateArray_189.rotate(nums = [1,2,3,4,5,6,7], k = 3), [5,6,7,1,2,3,4])
        
    def test_2(self):
        self.assertEqual(RotateArray_189.rotate(nums = [-1,-100,3,99], k = 2), [3,99,-1,-100])
        

    
if __name__ == '__main__':
    unittest.main()