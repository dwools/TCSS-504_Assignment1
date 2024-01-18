import random


class MineGenerator:

    def __init__(self):
        pass

    def field_generator(self):

        row_count = random.randint(1, 5)
        col_count = random.randint(1, 5)

        output_file.write(f"{col_count} {row_count}\n")

        field = []

        for column in range(col_count):
            the_row = []
            field.append(the_row)

            for row in range(row_count):
                the_row.append(random.choice('.*'))

        joiner = [["".join(row)] for row in field]
        for x in joiner:
            row = str(x)
            output_file.write(f"{row}" + "\n")

    def run(self):
        num_of_tests = random.randint(5, 10)
        for num in range(num_of_tests):
            self.field_generator()


if __name__ == "__main__":
    output_file = open('mines.txt', 'w')
    file = MineGenerator()
    file.run()
    output_file.close()
