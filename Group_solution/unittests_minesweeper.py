import unittest
from minesweeper import Minesweeper

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
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

    def test_row_read(self):
        """Test to ensure rows are read in properly"""
        pass

    def test_column_read(self):
        """Test to ensure columns are read in properly"""
        pass

    def test_minimum_empty(self):
        """Test solution for ensure a 1x1 bombless minefield returns a 1x1 minefield with """
        minimum_empty_solution = open("test_minimum_empty_solution.txt", "r")
        self.solution = ''
        self.line = minimum_empty_solution.readline().strip('\n')
        self.solution += f'{self.line}\n'
        while self.line:
            if self.line == '\n':
                break
            else:
                self.line = minimum_empty_solution.readline().strip('\n')
                self.solution += f"{self.line}\n"

        minimum_empty_test = Minesweeper("test_minimum_empty")
        self.assertEqual(minimum_empty_test.output, self.solution, "Solutions aren't equal")
        minimum_empty_solution.close()

    def test_minimum_bomb(self):
        pass

    def test_bomb_counts(self):
        """Test to ensure clues for every possible quantity and position of neighboring bombs are lain properly."""
        minimum_empty_solution = open("test_minimum_empty_solution.txt", "r")
        self.solution = ''
        self.line = minimum_empty_solution.readline().strip('\n')
        self.solution += f'{self.line}\n'
        while self.line:
            if self.line == '\n':
                break
            else:
                self.line = minimum_empty_solution.readline().strip('\n')
                self.solution += f"{self.line}\n"

        minimum_empty_test = Minesweeper("test_bomb_count")
        self.assertEqual(minimum_empty_test.output, self.solution, "Solutions aren't equal")
        minimum_empty_solution.close()

    def test_maximum(self):

        pass


    def test_random(self):
        pass



if __name__ == '__main__':
    unittest.main()


