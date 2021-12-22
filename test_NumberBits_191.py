import NumberBits_191# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(NumberBits_191.hammingWeight(n='00000000000000000000000000001011'),3)
        
    def test_2(self):
        self.assertEqual(NumberBits_191.hammingWeight(n = '00000000000000000000000010000000'),1)
        
    def test_3(self):
        self.assertEqual(NumberBits_191.hammingWeight(n = '11111111111111111111111111111101'),31)
    
if __name__ == '__main__':
    unittest.main()