from Bingo import Bingo
from InputReader import InputReader

bingo = Bingo()

InputReader.read_file_to_function(
    "DayFourInput.txt",
    bingo.parse_line,
    ignore_first=True,
    special_first=bingo.input_numbers,
)

result = bingo.play()
print(f"The board with the number {result[0]} won! - The final score is {result[1]}.")
