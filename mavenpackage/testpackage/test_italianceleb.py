import unittest
import sys
import os
from mavenpackage import italianceleb


'''
The following tests are applied to the italianceleb function.
First, valid entries are tested: the function receives expected inputs.
Next, the function is given invalid entries and its reaction is checked.
Then, the performance when no inputs are provided is evaluated.
'''

class TestInput(unittest.TestCase):

    # smoke test: valid inputs
    def test_italianholidays(self):
        # you should select some valid inputs, for which the output is known
        self.assertEqual(italianceleb.italianceleb("All Saints' Day"), "Yup, {} is an Italian holiday!".format(someholi))

    # invalid inputs
    def test_nonitalian(self):
        # you should input wrong data
        self.assertEqual(italianceleb.italianceleb("Thanksgiving Day"), None)

        # Note: the following test passing an empty list will fail!
        # self.assertEqual(italianceleb([]), None)

    # corner case: empty string
    def test_emptyentry(self):
        self.assertEqual(italianceleb.italianceleb(""), None)

# code that runs the document if called
if __name__ == '__main__':
    unittest.main()

