from Submarine import Submarine
from InputReader import InputReader

submarine = Submarine()
diagnostic = submarine.diagnostic
InputReader.read_file_to_function("DayThreeInput.txt", diagnostic.parse_line)

print(f"0 is right-most!!! 11 is left-most!!!\n{diagnostic.ones}")
print(f"Solution: {diagnostic.gamma() * diagnostic.epsilon()}")

print(sorted(diagnostic.ones.keys(), reverse=True))

print(f"Soluteion task2: {diagnostic.search_oxygen_reading()[0] * diagnostic.search_carbon_reading()[0]}")

print(diagnostic.search_oxygen_reading())
print(diagnostic.search_carbon_reading())


"""debug_submarine = Submarine()
debug_diagnostic = debug_submarine.diagnostic
debug_vals = [
    int("00100",2),
    int("11110",2),
    int("10110",2),
    int("10111",2),
    int("10101",2),
    int("01111",2),
    int("00111",2),
    int("11100",2),
    int("10000",2),
    int("11001",2),
    int("00010",2),
    int("01010",2)
]
for val in debug_vals:
    debug_diagnostic.analyze(val)

# print(debug_diagnostic.search_oxygen_reading()[0] * debug_diagnostic.search_carbon_reading()[0])

print(debug_diagnostic.search_oxygen_reading())
print(debug_diagnostic.search_carbon_reading())
"""