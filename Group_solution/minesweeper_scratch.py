import random
from input_generator import MineGenerator
from minesweeper import MinesweeperSolver

# ChatGPT-generated code:

def generate_minefield(rows, cols, mine_percentage):
    minefield = [['.' for _ in range(cols)] for _ in range(rows)]
    num_mines = int(rows * cols * mine_percentage/100)

    for _ in range(num_mines):
        while True:
            row = random.randint(0, rows - 1)
            col = random.randint(0, cols - 1)
            if minefield[row][col] != '*':
                minefield[row][col] = '*'
                break

    return minefield

if __name__ == '__main__':
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
    print(test_rows-1)

    columns = 0
    for character in test_line:
        columns += 1
    print(columns)

    # test_solution = open('minesweeper_input_output.txt', 'r')
    # test_solution.readline().strip('\n')
    # test_solution_line = test_solution.readline().strip('\n')
    #
    # test_solution_rows = 0
    # for line in test_solution:
    #     test_solution_rows += 1
    # print(test_solution_rows)
    #
    # test_solution_columns = 0
    # for character in test_solution_line:
    #     test_solution_columns += 1
    # print(test_solution_columns)

MineGenerator(100, 0, 0, 1)
test_0 = MinesweeperSolver()
print("output:" + test_0.output)


    # test_solution = open("minesweeper_input_output.txt", "r")
    # test_solution_dimensions =



