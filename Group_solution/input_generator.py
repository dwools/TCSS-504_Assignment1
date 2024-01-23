import random


class MineGenerator:
    """Generates string of a random or specified number of minefields, of random or specified bomb probability and dimensions, and writes the minefield strings into a text file to be passed into the MinesweeperSolver class and solved. """
    def __init__(self, bomb_percentage=None, row_count=None, col_count=None, num_of_tests=None):
        self.bomb_percentage = bomb_percentage
        self.row_count = row_count
        self.col_count = col_count
        self.num_of_tests = num_of_tests
        self.output_file = open('minesweeper_input.txt', 'w')
        self.run()

    def field_generator(self):
        """Assemble a string of minefields according to the specified bomb_percentage, row_count, col_count, and num_of_tests parameters. If no parameter is specified, randomize the unspecified parameter.
        Establish minefield and row as a blank string.
        1. Write a line indicating the number of specified or randomly-acquired rows and columns for each minefield.
        2. Over the specified or randomly-acquired col_count (AKA number of characters in a row), lay down a blank space (".") or a bomb ("*") according to the specified or randomly-acquired bomb_percentage to produce a "row" string.
        3. Over the specified or randomly-acquired row_count, write each "row" string into the "minefield" string.
        """

        #### Jackson's original code

        # if self.row_count or self.col_count is None:
        #     self.row_count = random.randint(1, 100)
        #     self.col_count = random.randint(1, 100)
        #
        # self.output_file.write(f"{self.row_count} {self.col_count}\n")
        #
        # minefield = ''
        # for i in range(self.row_count):
        #     row = ''
        #     for j in range(self.col_count):
        #         if random.randint(1, int(self.bomb_odds)) == 1:
        #             row += "*"
        #         else:
        #             row += "."
        #     minefield += f'{row}\n'
        # self.output_file.write(minefield)

        ##### David's code

        if self.row_count or self.col_count is not None:
            self.output_file.write(f"{self.row_count} {self.col_count}\n")
            minefield = ''
            for i in range(self.row_count):
                row = ''
                for j in range(self.col_count):
                    if self.bomb_percentage is None:
                        self.bomb_percentage = random.randint(1,100)
                        lay_bomb = random.randint(1, 100)
                        if lay_bomb <= self.bomb_percentage:
                            row += '*'
                        else:
                            row += '.'
                        self.bomb_percentage = None
                    else:
                        if self.bomb_percentage == 0:
                            row += '.'
                        elif random.randint(1, 100) <= self.bomb_percentage:
                            row += "*"
                        else:
                            row += "."
                minefield += f'{row}\n'
            self.output_file.write(minefield)

        else:
            self.row_count = random.randint(1, 100)
            self.col_count = random.randint(1, 100)
            self.output_file.write(f"{self.row_count} {self.col_count}\n")

            minefield = ''
            for i in range(self.row_count):
                row = ''
                for j in range(self.col_count):
                    if self.bomb_percentage is None:
                        self.bomb_percentage = random.randint(1, 100)
                        lay_bomb = random.randint(1, 100)
                        if lay_bomb <= self.bomb_percentage:
                            row += '*'
                        else:
                            row += '.'
                        self.bomb_percentage = None
                    else:
                        if self.bomb_percentage == 0:
                            row += '.'
                        elif random.randint(1, 100) <= self.bomb_percentage:
                            row += "*"
                        else:
                            row += "."
                minefield += f'{row}\n'
            self.output_file.write(minefield)
            self.row_count = None
            self.col_count = None

    def run(self):
        """ Write the minefields into a text file to be passed into the MinesweeperSolver class and solved.
        1. For a specified or randomly-acquired number of tests, run the field_generator method above.
        2. After all minefields have been generated, print "0 0" at the end of the text file to provide the MinesweeperSolver's termination condition.
        """
        if self.num_of_tests is None:
            self.num_of_tests = random.randint(5, 10)
        for num in range(self.num_of_tests):
            if self.row_count == 0 or self.col_count == 0:
                break
            else:
                self.field_generator()
        self.output_file.write("0 0\n\n")
        self.output_file.close()


if __name__ == "__main__":
   MineGenerator(100, 0,0, 5)
