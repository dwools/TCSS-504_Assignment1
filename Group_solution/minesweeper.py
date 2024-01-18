from input_generator import MineGenerator
import random
# Render the minesweeper solution into OOP program to call it in the unit tests
class MinesweeperSolver():
    """
    The code below reads the input file ("input_file") line by line and writes an output file ("output_file") containing the minesweeper clues for each field.
    Our output_file consists of a string called "output". Our "output" string consists of "minefield" strings, which consist of "row" strings. Each "row" is a string of bombs and clues.
    As the code reads in the input_file, the "output" string is assembled as follows:
        1) Split the dimension lines into n and m values.
        2) Append the characters in each non-dimension line into a list called "line_list".
        3) Append each "line_list" into a list, yielding a list of lists (LOL) called "field".
        4) Iterating through the LOL, check each cells' neighboring cells for bombs, and count the number of neighboring bombs.
        5) Update the "row" string with each cell's adjacent bomb count.
        6) Update the "minefield" string with each "row" string.
        7) Update the "output" string with each Field # and with each "minefield" string.
    """
    def __init__(self, input_file):
        MineGenerator().run()
        self.input_file = input_file
        self.solution_file = open(f"{self.input_file}_output.txt", "w")
        self.input_file = open(f"{self.input_file}.txt", "r")
        # self.generate_and_solve()


    # def solve(self):
        self.line = self.input_file.readline().strip('\n') # Prime the first line, and define "line" for our while loop.
        self.output = ''         # Our output is a string of "minefield" strings, which consist of "row" strings. Each row is a string of bombs and clues. We prime our output string here.
        self.field_number = 0    # Our output string also contains "Field #" headers. We prime this here.
        self.adjacent_bombs = 0
        while self.line:
            self.field = []
            self.minefield = ''  # Our output is a string of "minefield" strings, which consist of "row" strings. Each row is a string of bombs and clues. We prime (and reset) our "minefield" string here.
            self.row = ''        # Our output is a string of "minefield" strings, which consist of "row" strings. Each row is a string of bombs and clues. We prime our "row" string here.
            self.lines, self.length = self.line.split() # "line" is currently a string of two numbers representing the minefield dimensions. Split dimension line into individual characters "lines" and "length" (AKA n and m values)
            self.lines = int(self.lines)
            self.length = int(self.length)
            if self.lines == 0:                   # The final line is "0 0". Only the final row has a 0 in it. Thus, this is our termination condition.
                break                       # Stop code when we get to the final line, which reads "0 0"
            self.line = self.input_file.readline().strip('\n') # This reads in the first field line.


            ### Here, we render each field as an n x m list of lists called "field", whereby n = lines, m = length.
            for i in range(self.lines):          # "lines" acquired in line 27 and 28.
                self.line_list = list(self.line)      # Append each character in a line to a list called "line_list"
                self.field.append(self.line_list)     # Append each line_list to a list called "field".
                self.line = self.input_file.readline().strip('\n') # Read in the next line to iterate.

            ### Here, we iterate over our field (defined in line 38 and specified as our subject of iteration in line 81) to lay down the number of bombs adjacent to each cell and assemble our "row" string.
            # North neighbor: field[i-1][j]
            # South neighbor: field[i+1][j]
            # West neighbor: field[i][j-1]
            # East neighbor: field[i][j+1]
            # i-1 and j-1 must be >= 0
            # i+1 must be < lines
            # j+1 must be < length
            for i in range(self.lines):          # "lines" defined in line 27 and 28
                self.row = ''                    # We reset our row string here.
                for j in range(self.length):     # "length" defined in line 27 and 29
                    if self.field[i][j] != "*":
                            if i-1 >= 0 and self.field[i - 1][j] == "*":  # Check for bombs to the North.
                                self.adjacent_bombs += 1
                            if i-1 >= 0 and j+1 < self.length and self.field[i - 1][j + 1] == "*":  # Check for bombs to the Northeast
                                self.adjacent_bombs += 1
                            if j+1 < self.length and self.field[i][j + 1] == "*":  # Check for bombs to the East
                                self.adjacent_bombs += 1
                            if i+1 < self.lines and j+1 < self.length and self.field[i + 1][j + 1] == "*":  # Check for bombs to the Southeast
                                self.adjacent_bombs += 1
                            if i+1 < self.lines and self.field[i + 1][j] == "*":  # Check for bombs to the South
                                self.adjacent_bombs += 1
                            if i+1 < self.lines and j-1 >= 0 and self.field[i + 1][j - 1] == "*":  # Check for bombs to the Southwest
                                self.adjacent_bombs += 1
                            if j-1 >= 0 and self.field[i][j - 1] == "*":  # Check for bombs to the West
                                self.adjacent_bombs += 1
                            if i-1 >= 0 and j-1 >= 0 and self.field[i - 1][j - 1] == "*":  # Check for bombs to the Northwest
                                self.adjacent_bombs += 1
                            self.row += str(self.adjacent_bombs)      # Here we update our "row" string of bombs and clues."
                            self.adjacent_bombs = 0          # Reset the adjacent bomb count for re-iteration.
                    else: self.row += "*"    # If a cell is a bomb, we skip the neighbor checking and update our row string with a bomb.
                self.minefield += f"{self.row}\n" # We update our minefield string with the above-assembled row string.
            self.field_number += 1           # Here we update our field number (defined in line 56) to be used in the "Field #" header above each field in our output.
            self.output += (f"Field #{str(self.field_number)}:\n{str(self.minefield)}\n") # Here we update our "output" string with our "Field #" header (defined in line 56 and updated in line 101) and with our above assembled "minefield" string.
        # print(self.output)
        self.solution_file.write(f"{self.output}")
        self.input_file.close()
        self.solution_file.close()

    def __str__(self):
        return self.output
    
    # def generate_and_solve(self):
    #     self.MineGenerator.run()
    #     self.solve()
# print(output)

# input_file = open('mines_simple.txt', 'r')

# if __name__ == '__main__':
    # test_minimum_empty = Minesweeper("test_minimum_empty")
    # test_bomb_count = Minesweeper("test_bomb_count_inputn()
    # file = MineGenerator()
    # file.run()

    # print(MinesweeperSolver("test_bomb_counts_input").output)

# bomb_counts_solution = open("test_bomb_counts_solution.txt", "r")
# solution = ''
# # line = bomb_counts_solution.readline().strip('\n')
# # solution += f'{line}\n'
# for line in bomb_counts_solution:
#     # if line == "0 0":
#     #     break
#     # else:
#     solution += f"{line}"
#     # line = bomb_counts_solution.readline().strip('\n')
#
# print(solution)

