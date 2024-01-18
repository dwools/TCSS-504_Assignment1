import random
import unittest
from minesweeper import MinesweeperSolver

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
        """Test solution for ensure a 1x1 bombless minefield returns a 1x1 minefield with a 1x1 solution whose clue is 0"""
        minimum_empty_solution = open("test_minimum_empty_solution.txt", "r")
        self.solution = ''
        for line in minimum_empty_solution:
            self.solution += f"{line}"

        test_minimum_empty = MinesweeperSolver("test_minimum_empty_input")
        self.assertEqual(test_minimum_empty.output, self.solution, "Solutions aren't equal")
        minimum_empty_solution.close()

    def test_minimum_bomb(self):
        """Test solution for ensure a 1x1 minefield minefield containing a single bomb returns a 1x1 solution with a single bomb."""
        minimum_bomb_solution = open("test_minimum_bomb_solution.txt", "r")
        self.solution = ''
        for line in minimum_bomb_solution:
            self.solution += f"{line}"

        test_minimum_bomb = MinesweeperSolver("test_minimum_bomb_input")
        self.assertEqual(test_minimum_bomb.output, self.solution, "Solutions aren't equal")
        minimum_bomb_solution.close()

    def test_bomb_counts(self):
        """Test to ensure clues for every possible quantity and position of neighboring bombs are laid properly."""
        bomb_counts_solution = open("test_bomb_counts_solution.txt", "r")
        self.solution = ''
        for line in bomb_counts_solution:
            self.solution += f'{line}'

        test_bomb_counts = MinesweeperSolver("test_bomb_counts_input")
        self.assertEqual(test_bomb_counts.output, self.solution, "Solutions aren't equal")
        bomb_counts_solution.close()

    def test_edge(self):
        edge_solution = open("test_edge_solution.txt", "r")
        self.solution = ''
        for line in edge_solution:
            self.solution += line

        test_edge = MinesweeperSolver("test_edge_input")
        self.assertEqual(test_edge.output, self.solution, "Solutions aren't equal")
        edge_solution.close()


    def test_maximum(self):


        pass


    def test_random(self):
        pass



if __name__ == '__main__':
    unittest.main()


