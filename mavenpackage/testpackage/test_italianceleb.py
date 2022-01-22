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

    # Smoke test: valid inputs
    def test_italianholidays(self):
        # you should select some valid inputs, for which the output is known
        self.assertEqual(italianceleb.italianceleb("All Saints' Day"), "Yup,"+
       " All Saints' Day is an Italian holiday!")

    def test_nonitalian(self):
       # You should input wrong data
       self.assertEqual(italianceleb.italianceleb("Thanksgiving Day"), "Nope"+
       ", Italians do not celebrate Thanksgiving Day.")

    # Invalid inputs
    def test_wrongvalues(self):
       # You should input wrong data
       self.assertEqual(italianceleb.italianceleb("78"), "Nope"+
       ", Italians do not celebrate 78.")

    # Corner case: empty string
    def test_emptyentry(self):
        self.assertEqual(italianceleb.italianceleb(""), "Nope"+
       ", Italians do not celebrate .")


# Code that runs the document if called
if __name__ == "__main__":
    unittest.main()
