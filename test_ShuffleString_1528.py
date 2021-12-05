import ShuffleString_1528  # The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(ShuffleString_1528.restoreString("codeleet",[4,5,6,7,0,2,1,3]), "leetcode")
    
    def test_2(self):
        self.assertEqual(ShuffleString_1528.restoreString("abc",[0,1,2]), "abc")
    
    def test_3(self):
        self.assertEqual(ShuffleString_1528.restoreString("aiohn", [3,1,4,2,0]), "nihao")
    
    def test_4(self):
        self.assertEqual(ShuffleString_1528.restoreString(s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]), "arigatou")
        
    def test_5(self):
        self.assertEqual(ShuffleString_1528.restoreString(s = "art", indices = [1,0,2]), "rat")
    

if __name__ == '__main__':
    unittest.main()