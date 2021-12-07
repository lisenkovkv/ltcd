import  GoalParserInterpretation_1678 # The code to test
import unittest   # The test framework

class Test_JewelsandStones_771(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(GoalParserInterpretation_1678.interpret(command = "G()(al)"), "Goal")
    
    def test_2(self):
        self.assertEqual(GoalParserInterpretation_1678.interpret(command = "G()()()()(al)"), "Gooooal")
    
    def test_3(self):
        self.assertEqual(GoalParserInterpretation_1678.interpret(command = "(al)G(al)()()G"), "alGalooG")
    

if __name__ == '__main__':
    unittest.main()