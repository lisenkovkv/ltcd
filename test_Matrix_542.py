import Matrix_542# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(Matrix_542.updateMatrix(mat = [[0,0,0],[0,1,0],[0,0,0]]),[[0,0,0],[0,1,0],[0,0,0]])
    
    def test_2(self):
        self.assertEqual(Matrix_542.updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]]),[[0,0,0],[0,1,0],[1,2,1]])
    
if __name__ == '__main__':
    unittest.main()