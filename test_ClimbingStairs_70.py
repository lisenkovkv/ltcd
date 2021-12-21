import ClimbingStairs_70# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(ClimbingStairs_70.climbStairs(n = 2),2)
    
    def test_2(self):
        self.assertEqual(ClimbingStairs_70.climbStairs(n = 3),3)

    
if __name__ == '__main__':
    unittest.main()