import unittest
import sys
import os
import datetime
from dateutil.relativedelta import relativedelta
from mavenpackage import countdown

'''
The following tests are applied to the countdown function.
The standard testing order is followed.
'''

class TestInput(unittest.TestCase):

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
