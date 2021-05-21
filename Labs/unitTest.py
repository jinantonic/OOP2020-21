import unittest
from Labs.unitTest import TestCalculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.status = unitTest([2, 4, 6, 8, 10])

    def calculate(self, a, b):
        return a * b

    def teat_correct_calc(self):
        pass

    # test that an assertion is thrown
    @unittest.expectedFailure
    def test_incorrect_calc(self, a, b):
        return a * b

if __name__ == "__main__":
    unittest.main() # Calls the main method for the unittest