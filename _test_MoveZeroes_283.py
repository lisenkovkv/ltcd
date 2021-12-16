import MoveZeroes_283# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(MoveZeroes_283.moveZeroes(nums = [0,1,0,3,12]), [1,3,12,0,0])
        
    def test_2(self):
        self.assertEqual(MoveZeroes_283.moveZeroes(nums = [0]), [0])
        

    
if __name__ == '__main__':
    unittest.main()