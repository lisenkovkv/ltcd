import Triangle_120# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(Triangle_120.minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]),11)
    
    def test_2(self):
        self.assertEqual(Triangle_120.minimumTotal(triangle = [[-10]]),-10)

    
if __name__ == '__main__':
    unittest.main()