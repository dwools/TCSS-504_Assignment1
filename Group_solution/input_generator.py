import random


class MineGenerator:

    def __init__(self, bomb_odds = 5):
        self.bomb_odds = bomb_odds
        self.output_file = open('mines.txt', 'w')

    def field_generator(self):

        row_count = random.randint(1, 10)
        col_count = random.randint(1, 10)

        self.output_file.write(f"{row_count} {col_count}\n")

        minefield = ''
        for i in range(row_count):
            row = ''
            for j in range(col_count):
                if random.randint(1, int(self.bomb_odds)) == 1:
                    row += "*"
                else:
                    row += "."
                # row += random.choice('...*')
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

