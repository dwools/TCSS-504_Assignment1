import random
import unittest
from minesweeper import MinesweeperSolver
from input_generator import MineGenerator

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

    def test_rows_columns_read(self):
        """Test to ensure rows and columns are read in properly during minefield generation and solving"""
        MineGenerator(5, 10, 20, 1)
        MinesweeperSolver()
        test = open("minesweeper_input.txt", "r")

        test_dimensions = test.readline().strip('\n')
        read_rows, read_columns = test_dimensions.split()
        print(read_rows, read_columns)
        test_line = test.readline().strip('\n')

        test_rows = 0
        for line in test:
            test_rows += 1
        test_rows = test_rows-1

        test_columns = 0
        for character in test_line:
            test_columns += 1

        self.assertEqual(test_rows, 10, "test_rows should be 10")
        self.assertEqual(test_columns, 20, "test_columns should be 20")

        test_solution = open('minesweeper_input_output.txt', 'r')
        test_solution.readline().strip('\n')
        test_solution_line = test_solution.readline().strip('\n')

        test_solution_rows = 0
        for line in test_solution:
            test_solution_rows += 1


        test_solution_columns = 0
        for character in test_solution_line:
            test_solution_columns += 1

        self.assertEqual(test_solution_rows, 10, "test_solution_rows should be 10")
        self.assertEqual(test_solution_columns, 20, "test_solution_rows should be 20")
        self.assertEqual(test_rows, test_solution_rows, "Test and solution rows are different")
        self.assertEqual(test_columns, test_solution_columns, "Test and solution columns are different")


    def test_minimum_empty(self):
        """Test solution for ensure a 1x1 bombless minefield returns a 1x1 minefield with a 1x1 solution whose clue is 0"""
        minimum_empty_solution = open("test_minimum_empty_solution.txt", "r")
        self.solution = ''
        for line in minimum_empty_solution:
            self.solution += f"{line}"

        MineGenerator(0,1,1,1)
        test_minimum_empty = MinesweeperSolver()
        self.assertEqual(test_minimum_empty.output, self.solution, "Solutions aren't equal")

    def test_minimum_bomb(self):
        """Test solution for ensure a 1x1 minefield minefield containing a single bomb returns a 1x1 solution with a single bomb."""

        minimum_bomb_solution = open("test_minimum_bomb_solution.txt", "r")
        self.solution = ''
        for line in minimum_bomb_solution:
            self.solution += f"{line}"

        MineGenerator(100, 1, 1, 1)
        test_minimum_bomb = MinesweeperSolver()
        self.assertEqual(test_minimum_bomb.output, self.solution, "Solutions aren't equal")

    def test_minimum_0(self):
        """Test generation and solving of a 0x0 minefield"""

        no_bomb_solution = open("test_0_solution.txt", "r")
        self.solution = ''
        for line in no_bomb_solution:
            self.solution += f"{line}"

        MineGenerator(100, 0, 0, 5)
        test_0 = MinesweeperSolver()
        self.assertEqual(test_0.output, self.solution, "Solutions aren't equal")


    def test_maximum_empty(self):
        """Test generation and solving of 10 empty 100x100 minefields"""
        maximum_empty_solution = open('test_maximum_empty_solution.txt', 'r')
        self.solution = ''
        for line in maximum_empty_solution:
            self.solution += line

        MineGenerator(0,100,100,10)
        test_maximum_empty = MinesweeperSolver()
        self.assertEqual(test_maximum_empty.output, self.solution, "Solutions aren't equal")

    def test_maximum_bombs(self):
        """Test generation and solving of 10 full (all bombs) 100x100 minefields"""
        maximum_bombs_solution = open('test_maximum_bombs_solution.txt', 'r')
        self.solution = ''
        for line in maximum_bombs_solution:
            self.solution += line

        MineGenerator(100, 100, 100, 10)
        test_maximum_bombs = MinesweeperSolver()
        self.assertEqual(test_maximum_bombs.output, self.solution, "Solutions aren't equal")

    def test_bomb_counts(self):
        """Test to ensure clues for every possible quantity and position of neighboring bombs are laid properly."""
        bomb_counts_solution = open("test_bomb_counts_solution.txt", "r")
        self.solution = ''
        for line in bomb_counts_solution:
            self.solution += f'{line}'

        test_bomb_counts = MinesweeperSolver("test_bomb_counts_input")
        self.assertEqual(test_bomb_counts.output, self.solution, "Solutions aren't equal")
        bomb_counts_solution.close()

    def test_edges(self):
        """Test that minefield edges are working properly """
        edge_solution = open("test_edge_solution.txt", "r")
        self.solution = ''
        for line in edge_solution:
            self.solution += line

        test_edge = MinesweeperSolver("test_edge_input")
        self.assertEqual(test_edge.output, self.solution, "Solutions aren't equal")
        edge_solution.close()





if __name__ == '__main__':
    unittest.main()


