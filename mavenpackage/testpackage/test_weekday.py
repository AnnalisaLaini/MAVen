import unittest
import sys
import os
from mavenpackage import weekday



'''
The following tests are applied to the weekday function.
The standard testing order is followed.
'''

class TestInput(unittest.TestCase):

    # smoke test: valid inputs

    def test_correct_values(self):
        # you should select some valid inputs, for which the output is known
        self.assertEqual(weekday("Monday"), "2022-01-10")       
    
    # invalid inputs

    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(weekday("2022-05-10"), "Wednesday")  
        self.assertEqual(weekday("seven"), "None") 

       #NOTE: the folowing test passing an empty list will fail!
       #self.assertEqual (weekday(), None)  


    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(weekday(""), None)

#code that runs the document if called
if __name__ == '__main__':
    unittest.main()

