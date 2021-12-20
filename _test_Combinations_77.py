import Combinations_77# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(Combinations_77.combine(n = 4, k = 2),[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])

    def test_2(self):
        self.assertEqual(Combinations_77.combine(n = 1, k = 1),[[1]])
    
if __name__ == '__main__':
    unittest.main()