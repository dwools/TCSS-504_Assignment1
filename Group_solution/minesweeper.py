
# Render the minesweeper solution into OOP program to call it in the unit tests
class Minesweeper():
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

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def solve(self):
        line = self.input_file.readline().strip('\n') # Prime the first line, and define "line" for our while loop.
        output = ''         # Our output is a string of "minefield" strings, which consist of "row" strings. Each row is a string of bombs and clues. We prime our output string here.
        field_number = 0    # Our output string also contains "Field #" headers. We prime this here.
        adjacent_bombs = 0
        while line:
            field = []
            minefield = ''  # Our output is a string of "minefield" strings, which consist of "row" strings. Each row is a string of bombs and clues. We prime (and reset) our "minefield" string here.
            row = ''        # Our output is a string of "minefield" strings, which consist of "row" strings. Each row is a string of bombs and clues. We prime our "row" string here.
            lines, length = line.split() # "line" is currently a string of two numbers representing the minefield dimensions. Split dimension line into individual characters "lines" and "length" (AKA n and m values)
            lines = int(lines)
            length = int(length)
            if lines == 0:                   # The final line is "0 0". Only the final row has a 0 in it. Thus, this is our termination condition.
                break                       # Stop code when we get to the final line, which reads "0 0"
            line = input_file.readline().strip('\n') # This reads in the first field line.


            ### Here, we render each field as an n x m list of lists called "field", whereby n = lines, m = length.
            for i in range(lines):          # "lines" acquired in line 27 and 28.
                line_list = list(line)      # Append each character in a line to a list called "line_list"
                field.append(line_list)     # Append each line_list to a list called "field".
                line = input_file.readline().strip('\n') # Read in the next line to iterate.

            ### Here, we iterate over our field (defined in line 38 and specified as our subject of iteration in line 81) to lay down the number of bombs adjacent to each cell and assemble our "row" string.
            # North neighbor: field[i-1][j]
            # South neighbor: field[i+1][j]
            # West neighbor: field[i][j-1]
            # East neighbor: field[i][j+1]
            # i-1 and j-1 must be >= 0
            # i+1 must be < lines
            # j+1 must be < length
            for i in range(lines):          # "lines" defined in line 27 and 28
                row = ''                    # We reset our row string here.
                for j in range(length):     # "length" defined in line 27 and 29
                    if field[i][j] != "*":
                            if i-1 >= 0 and field[i - 1][j] == "*":  # Check for bombs to the North.
                                adjacent_bombs += 1
                            if i-1 >= 0 and j+1 < length and field[i - 1][j + 1] == "*":  # Check for bombs to the Northeast
                                adjacent_bombs += 1
                            if j+1 < length and field[i][j + 1] == "*":  # Check for bombs to the East
                                adjacent_bombs += 1
                            if i+1 < lines and j+1 < length and field[i + 1][j + 1] == "*":  # Check for bombs to the Southeast
                                adjacent_bombs += 1
                            if i+1 < lines and field[i + 1][j] == "*":  # Check for bombs to the South
                                adjacent_bombs += 1
                            if i+1 < lines and j-1 >= 0 and field[i + 1][j - 1] == "*":  # Check for bombs to the Southwest
                                adjacent_bombs += 1
                            if j-1 >= 0 and field[i][j - 1] == "*":  # Check for bombs to the West
                                adjacent_bombs += 1
                            if i-1 >= 0 and j-1 >= 0 and field[i - 1][j - 1] == "*":  # Check for bombs to the Northwest
                                adjacent_bombs += 1
                            row += str(adjacent_bombs)      # Here we update our "row" string of bombs and clues."
                            adjacent_bombs = 0          # Reset the adjacent bomb count for re-iteration.
                    else: row += "*"    # If a cell is a bomb, we skip the neighbor checking and update our row string with a bomb.
                minefield += f"{row}\n" # We update our minefield string with the above-assembled row string.
            field_number += 1           # Here we update our field number (defined in line 56) to be used in the "Field #" header above each field in our output.
            output += (f"Field #{str(field_number)}:\n" # Here we update our "output" string with our "Field #" header (defined in line 56 and updated in line 101) and with our above assembled "minefield" string.
                       f"{str(minefield)}\n")
# print(output)

# input_file = open('mines_simple.txt', 'r')

if __name__ == '__main__':
    unittest.main()



    input_file = open('mines.txt', 'r')
    output_file = open('minesweeper_output.txt', 'w')


    output_file.write(f"{output}")
    input_file.close()
    output_file.close()

