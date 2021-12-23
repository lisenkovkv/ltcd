import ReverseBits_190# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(ReverseBits_190.reverseBits(n = '00000010100101000001111010011100'),964176192)
        
    def test_2(self):
        self.assertEqual(ReverseBits_190.reverseBits(n = '11111111111111111111111111111101'),3221225471)
    
if __name__ == '__main__':
    unittest.main()