import unittest
import sys
import os
from dateutil.relativedelta import relativedelta
from mavenpackage import countdown.py
from countdown.py import countdown

'''
The following tests are applied to the countdown function.
The standard testing order is followed.
'''

class TestInput(unittest.TestCase):

   # smoke test: valid inputs
   def test_correct_values(self):
       # you should select some valid inputs, for which the output is known
       one_year_ago = datetime.date.today() - relativedelta(years=1)
       self.assertEqual(countdown(one_year_ago, "365 days have passed since the input date"))

   # invalid inputs
   def test_wrong_values(self):
       # you should input wrong data
       self.assertEqual(countdown("2022-01-32"), None)
       self.assertEqual(countdown("hello"), None)
       self.assertEqual(countdown("67"), None)

   # NOTE: the following test passing an empty list will fail!
   # self.assertEqual(countdown([]), None)

   # corner case: empty string
   def test_empty_string(self):
       self.assertEqual(countdown(""), None)

# code that runs the document if called
if __name__ == '__main__':
    unittest.main()
