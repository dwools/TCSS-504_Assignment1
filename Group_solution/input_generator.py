import random


class MineGenerator:

    def __init__(self, bomb_odds=5, row_count=None, col_count=None):
        self.bomb_odds = bomb_odds
        self.row_count = row_count
        self.col_count = col_count
        self.output_file = open('minesweeper_input.txt', 'w')

    def field_generator(self):
        if self.row_count or self.col_count is None:
            self.row_count = random.randint(1, 100)
            self.col_count = random.randint(1, 100)

        self.output_file.write(f"{self.row_count} {self.col_count}\n")

        minefield = ''
        for i in range(self.row_count):
            row = ''
            for j in range(self.col_count):
                if random.randint(1, int(self.bomb_odds)) == 1:
                    row += "*"
                else:
                    row += "."
            minefield += f'{row}\n'
        self.output_file.write(minefield)

    def run(self):
        num_of_tests = random.randint(5, 10)
        for num in range(num_of_tests):
            self.field_generator()
        self.output_file.write("0 0")
        self.output_file.close()


if __name__ == "__main__":
    file = MineGenerator()
    file.run()
