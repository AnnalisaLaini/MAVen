import unittest
import countdown

'''
The following tests are applied to the countdown function.
The standard testing order is followed.
'''


class TestInput(unittest.TestCase):
    # Invalid inputs
    def test_wrong_values(self):
        # You should input wrong data
        self.assertEqual(countdown.countdown("2022-01-32"), "Incorrect data " +
                         "format, should be YYYY-MM-DD")
        self.assertEqual(countdown.countdown("hello"), "Incorrect data " +
                         "format, should be YYYY-MM-DD")
        self.assertEqual(countdown.countdown("67"), "Incorrect data " +
                         "format, should be YYYY-MM-DD")

        # Corner case: empty string
    def test_empty_string(self):
        self.assertEqual(countdown.countdown(""), "Incorrect data " +
                         "format, should be YYYY-MM-DD")


# Code that runs the document if called
if __name__ == "__main__":
    unittest.main()
