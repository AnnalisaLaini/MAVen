import unittest
import sys
import os
from mavenpackage import weekday


'''
The following tests are applied to the weekday function.
The standard testing order is followed.
'''


class TestInput(unittest.TestCase):

    # Smoke test: valid inputs

    def test_correct_values(self):
        # You should select some valid inputs, for which the output is known
        self.assertEqual(weekday.weekday("2022-1-10"), "0")

    # Invalid inputs
    def test_wrong_values(self):
        # You should input wrong data
        self.assertEqual(weekday.weekday("Wednesday"), None)
        self.assertEqual(weekday.weekday("seven"), None)

        # NOTE: the folowing test passing an empty list will fail!
        # self.assertEqual (weekday.weekday(), None)

    # Corner case: empty string
    def test_empty_string(self):
        with self.assertRaises(TypeError):
            weekday()


# Code that runs the document if called
if __name__ == "__main__":
    unittest.main()
