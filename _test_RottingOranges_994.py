import RottingOranges_994# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(RottingOranges_994.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]),4)
    
    def test_2(self):
        self.assertEqual(RottingOranges_994.orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]),-1)
    
    def test_3(self):
        self.assertEqual(RottingOranges_994.orangesRotting(grid = [[0,2]]),0)
    
    
if __name__ == '__main__':
    unittest.main()