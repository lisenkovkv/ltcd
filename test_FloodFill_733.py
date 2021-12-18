import FloodFill_733# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(FloodFill_733.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2),[[2,2,2],[2,2,0],[2,0,1]])
    
    def test_2(self):
        self.assertEqual(FloodFill_733.floodFill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2),[[2,2,2],[2,2,2]])
 
if __name__ == '__main__':
    unittest.main()