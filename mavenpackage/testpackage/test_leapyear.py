import unittest
import sys
import os
from mavenpackage import leapyear


'''
The following tests are applied to the weekday function.
The standard testing order is followed.
'''


class TestInput(unittest.TestCase):

    # Smoke test: valid inputs
    def test_leapyear(self):
        # You should select some valid inputs, for which the output is known
        self.assertEqual(leapyear.leapyear("2000"), "'{0} is a leap \
        year'.format(year)")

    # Wrong inputs
    def test_not_leapyear1(self):
        # You should input wrong data
        self.assertEqual(leapyear("hello"), None)
        self.assertEqual(leapyear.leapyear("twothousand"), None)

    # Corner case: empty string
    def test_emptyentry(self):
        self.assertEqual(leapyear.leapyear(""), None)

# Code that runs the document if called
if __name__ == "__main__":
    unittest.main()
