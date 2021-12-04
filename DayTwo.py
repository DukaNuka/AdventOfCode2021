from InputReader import InputReader
from Submarine import Submarine


submarine = Submarine()
InputReader.read_file_to_function("DayTwoInput.txt", submarine.parse_line)
print(f"Solution task 1: {submarine.latitude * submarine.current_depth}")
