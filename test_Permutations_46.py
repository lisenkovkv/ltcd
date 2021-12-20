import Permutations_46# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(Permutations_46.permute(nums = [1,2,3]),[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])

    def test_2(self):
        self.assertEqual(Permutations_46.permute(nums = [0,1]),[[0,1],[1,0]])
    
    def test_3(self):
        self.assertEqual(Permutations_46.permute([1]),[[1]])
    
if __name__ == '__main__':
    unittest.main()