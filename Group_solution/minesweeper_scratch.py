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
    test = MineGenerator(1, 1, 1, 1)
    test.run()
    print(test)