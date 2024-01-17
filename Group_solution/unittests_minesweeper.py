import unittest
import minesweeper

### Make the minesweeper
class MyTestCase(unittest.TestCase):
    """ Build unit tests to test your team solution. Incorporate the results from your input generator into your unit tests as you deem necessary.
    Your tests should cover all edge cases (minimums, maximums) as well as some general cases.
    Recall that the input to the program will be well-formed so you are not required to test for invalid data.
There should be individual test methods for each case you test.
Include tests to ensure you can properly read in the rows, columns, and data for a single minefield.
Include tests that validate your hint producing code/function/method.
Include tests that validate output for a given minefield is formatted properly.
Be sure and name your test methods so they describe the test.
"""
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_row_read(self):
        """Test to ensure rows are read in properly"""
        pass

    def test_column_read(self):
        """Test to ensure columns are read in properly"""
        pass

    def test_minimum(self):
        pass

    def test_bomb_counts(self):
        """Test to ensure clues for every possible quantity and position of neighboring bombs are lain properly."""

    def test_maximum(self):

        pass


    def test_random(self):
        pass



if __name__ == '__main__':
    unittest.main()


