import RomantoInteger_13   # The code to test
import unittest   # The test framework

class Test_RomantoInteger(unittest.TestCase):
    
    def test_first(self):
        self.assertEqual(RomantoInteger_13.romanToInt('III'), 3)

    def test_second(self):
        self.assertEqual(RomantoInteger_13.romanToInt('IV'), 4)


if __name__ == '__main__':
    unittest.main()