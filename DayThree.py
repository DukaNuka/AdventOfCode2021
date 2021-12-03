from Submarine import Submarine
from InputReader import InputReader

submarine = Submarine()
diagnostic = submarine.diagnostic
InputReader.read_file_to_function("DayThreeInput.txt", diagnostic.parse_line)

print(f"Solution: {diagnostic.gamma() * diagnostic.epsilon()}")