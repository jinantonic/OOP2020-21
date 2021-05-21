# course: Object-oriented programming, year 2
# academic year: 2020-21
# author: Jina Park
# date: 21-05-2021
# purpose: OOP Semester 2 Exam


# imports
import unittest
import TestCalculator

# Testing class
class TestCalculator(unittest.TestCase):
    
    # Set up all necessary variables used during the test
    def setUp(self):
        self.stats = [2, 4, 6, 8, 10]

    def calculate(self, a, b):
        result = self.a * self.b
        self.assertEqual(result == a * b)

    def teat_correct_calc(self, a, b):
        result = self.a * self.b
        self.assertEqual(result == a * b)
        pass

    # Test that an assertion is thrown
    # This one fails initially.
    @unittest.expectedFailure
    def test_incorrect_calc(self, a, b):
        result = self.a * self.b
        self.assertEqual(result == a / b)
        
        
# Call the main method for the unittest
if __name__ == "__main__":
    unittest.main() 