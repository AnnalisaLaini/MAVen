import unittest
import return_event


'''
The following tests are applied to the return_event function.
First, valid entries are tested: the function receives expected inputs.
Next, the function is given invalid entries and its reaction is checked.
Then, the performance when no inputs are provided is evaluated.
'''


class TestInput(unittest.TestCase):

    # Smoke test: valid inputs
    def test_correct_values(self):
        # You should select some valid inputs, for which the output is known
        self.assertEqual(return_event.return_event("2023-12-26"),
                         "2023-12-26 is St. Stephen's Day.")

    # Invalid inputs
    def test_wrong_values(self):
        # You should input wrong data
        self.assertEqual(return_event.return_event("St. Stephen's Day"),
                         "Sadly, we don't know what is" +
                         "celebrated on St. Stephen's Day")

        # Note: the following test passing an empty list will fail!
        # self.assertEqual(return_event.return_event([]), None)

    # Corner case: empty string
    def test_empty_string(self):
        self.assertEqual(return_event.return_event(""),
                         "Sadly, we don't know what is" +
                         " celebrated on ")


# Code that runs the document if called
if __name__ == "__main__":
    unittest.main()
