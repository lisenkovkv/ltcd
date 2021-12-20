import MergeTwoSortedLists_21# The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(MergeTwoSortedLists_21.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]),[1,1,2,3,4,4])
    
    def test_2(self):
        self.assertEqual(MergeTwoSortedLists_21.mergeTwoLists(list1 = [], list2 = []),[])
        
    def test_3(self):
        self.assertEqual(MergeTwoSortedLists_21.mergeTwoLists(list1 = [], list2 = [0]),[0]) 
    
if __name__ == '__main__':
    unittest.main()