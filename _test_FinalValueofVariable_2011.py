import FinalValueofVariable_2011  # The code to test
import unittest   # The test framework

class Test_FinalValueofVariable_2011(unittest.TestCase):
    
    def test_first(self):
        self.assertEqual(FinalValueofVariable_2011.finalValueAfterOperations(["--X","X++","X++"]), 1)

    def test_second(self):
        self.assertEqual(FinalValueofVariable_2011.finalValueAfterOperations(["++X","++X","X++"]), 3)

    def test_third(self):
        self.assertEqual(FinalValueofVariable_2011.finalValueAfterOperations([]),0)

    def test_fourth(self):
        self.assertEqual(FinalValueofVariable_2011.finalValueAfterOperations(["X++","++X","--X","X--"]),0)

if __name__ == '__main__':
    unittest.main()