import unittest
import sys
import os
from mavenpackage import leapyear

class TestInput(unittest.TestCase):
    
    #smoke test: valid inputs
    def test_leapyear(self):
        # you should select some valid inputs, for which the output is known
        self.assertEqual(leapyear.leapyear("2000"), "'{0} is a leap year'.format(year)")
    
     #wrong inputs 
    def test_not_leapyear(self):
         # you should input wrong data
        self.assertEqual(leapyear("hello"), None)         

	#wrong inputs 
    def test_not_leapyear(self):
         # you should input wrong data
        self.assertEqual(leapyear.leapyear("twothousand"), None)

    # corner case: empty string
    def test_emptyentry(self):
        self.assertEqual(leapyear.leapyear(""), None)

  #code that runs the document if called
if __name__ == '__main__':
	unittest.main()
