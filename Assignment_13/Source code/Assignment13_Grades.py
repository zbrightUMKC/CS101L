import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):

    def test_tool_returns_total_of_list(self):

        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")
    
    def test_total_returns_0(self):

        result = Grades.total([])
        self.assertEqual(result, 0, "The empty function should return zero")

    def test_average_one(self):

        result = Grades.average([2, 5, 9])
        self.assertAlmostEqual(result, 5.33333, 5)
    
    def test_average_two(self):

        result = Grades.average([2, 15, 22, 9])
        self.assertAlmostEqual(result, 12.0000, 4)
    
    def test_average_returns_nan(self):

        result = Grades.average([])
        self.assertIs(result, math.nan)

    def test_median_returns_one(self):

        result = Grades.median([2, 5, 1])
        self.assertEqual(result, 2, "The median should return 2")
    
    def test_median_returns_two(self):

        result = Grades.median([3, 2, 5, 1])
        self.assertEqual(result, 2.5, "The median should return 2.5")
    
    def test_median_returns_ValueError(self):

        with self.assertRaises(ValueError):
            result = Grades.median([])


unittest.main()