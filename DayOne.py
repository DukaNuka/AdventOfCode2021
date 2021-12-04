from Sonar import Sonar
from InputReader import InputReader

sonar = Sonar()
InputReader.read_file_to_function("DayOneInput.txt", sonar.analyze_new_depth)
print(f"Solution task 1: {sonar.deeper}")
print(f"Solution task 2: {sonar.sum_deeper}")
