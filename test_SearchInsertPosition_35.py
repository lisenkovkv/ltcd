import SearchInsertPosition_35 # The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(SearchInsertPosition_35.searchInsert(nums = [1,3,5,6], target = 5), 2)
        
    def test_2(self):
        self.assertEqual(SearchInsertPosition_35.searchInsert(nums = [1,3,5,6], target = 2), 1)
        
    def test_3(self):
        self.assertEqual(SearchInsertPosition_35.searchInsert(nums = [1,3,5,6], target = 7), 4)
    
    def test_4(self):
        self.assertEqual(SearchInsertPosition_35.searchInsert(nums = [1,3,5,6], target = 0), 0)
        
    def test_4(self):
        self.assertEqual(SearchInsertPosition_35.searchInsert(nums = [1], target = 0), 0)

    
if __name__ == '__main__':
    unittest.main()