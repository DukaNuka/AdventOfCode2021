class BingoBoard:
    def __init__(self):
        self._numbers = []
        self._hit = []
        for i in range(5):
            self._hit.append([])
            for j in range(5):
                self._hit[i].append(False)

    def add_row(self, row):
        self._numbers.append(row)

    def check_win(self, i=0, j=0):
        return (
            i == 5
            or j == 5
            or (
                self._hit[i][j]
                and (
                    self.check_win(i=i + 1, j=j)
                    or self.check_win(i=i, j=j + 1)
                    or (i == j and self.check_win(i=i + 1, j=j + 1))
                )
            )
        )

    def sum_unchecked_numbers(self):
        calculated_sum = 0
        for i in range(len(self._numbers)):
            for j in range(len(self._numbers[i])):
                if not self._hit[i][j]:
                    calculated_sum += self._numbers[i][j]
        print(calculated_sum)
        return calculated_sum

    def check_hit(self, number: int):
        for i in range(len(self._numbers)):
            for j in range(len(self._numbers[i])):
                if self._numbers[i][j] == number:
                    self._hit[i][j] = True
        #print(f"Checking board for win\n{self.str()}")
        if self.check_win():
            return True
        else:
            return False

    def str(self):
        output = ""
        for i in range(len(self._numbers)):
            for j in range(len(self._numbers[i])):
                output += f"{self._numbers[i][j]}{'x' if self._hit[i][j] else ''} "
            output += "\n"
        return output


class Bingo:
    def __init__(self):
        self._numbers = []
        self._boards = []

    @property
    def numbers(self):
        return self._numbers

    @property
    def boards(self):
        return self._boards

    def input_numbers(self, numbers: str):
        print(numbers)
        self._numbers = [int(item) for item in numbers.split(",")]

    def generate_boards(self, boards: str):
        pass

    def play(self):
        for number in self._numbers:
            for current_board in range(len(self._boards)):
                if self._boards[current_board].check_hit(number):
                    return current_board + 1, self._boards[current_board].sum_unchecked_numbers() * number

    def parse_line(self, line):
        if len(line.split()) > 1:
            current_board = self._boards[-1]
            entries = [int(item) for item in line.split()]
            current_board.add_row(entries)
        else:
            self._boards.append(BingoBoard())
