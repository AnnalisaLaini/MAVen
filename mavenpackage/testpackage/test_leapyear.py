import unittest
import leapyear


'''
The following tests are applied to the weekday function.
The standard testing order is followed.
'''


class TestInput(unittest.TestCase):

    # Smoke test: valid inputs
    def test_leapyear(self):
        # You should select some valid inputs, for which the output is known
        self.assertEqual(leapyear.leapyear("2000"), "2000 is a leap year")

    # Wrong inputs
    def test_not_leapyear(self):
        # You should input wrong data
        self.assertEqual(leapyear.leapyear("hello"), 
                         "Input date is not valid")
        self.assertEqual(leapyear.leapyear("twothousand"), 
                         "Input date is not valid")

    # Corner case: empty string
    def test_emptyentry(self):
        self.assertEqual(leapyear.leapyear(""), "Input date is not valid")


# Code that runs the document if called
if __name__ == "__main__":
    unittest.main()
