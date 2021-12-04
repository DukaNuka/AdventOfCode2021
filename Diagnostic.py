import math
from collections import defaultdict


class Diagnostic:
    def __init__(self):
        self._history = []
        self._ones = defaultdict(int)

    @property
    def ones(self):
        return self._ones

    def analyze(self, value):
        self._history.append(value)
        if value != 0:
            for figure in range(int(math.log(value, 2)) + 1):
                if (value >> figure) & 1:
                    self._ones[figure] += 1

    def parse_line(self, line):
        self.analyze(int(line, 2))

    def gamma(self):
        # {0: 477, 1: 491, 2: 494, 4: 508, 5: 484, 7: 504, 8: 521, 9: 498, 10: 487, 11: 510, 6: 501, 3: 506}
        ret = 0
        for key in self._ones.keys():
            value = self._ones[key]
            if value > len(self._history) / 2:
                ret = ret | (1 << key)
        return ret

    def epsilon(self):
        gamma = self.gamma()
        return gamma ^ int("111111111111", 2)

    def search_oxygen_reading(self):
        values = self._history.copy()
        return self.get_oxygen_reading(values, 0)

    def get_oxygen_reading(self, values, bit):
        sub_diag = Diagnostic()
        new_values = []
        keys = sorted(self.ones.keys(), reverse=True)
        for value in values:
            sub_diag.analyze(value)
        if sub_diag.ones[keys[bit]] >= len(sub_diag._history) / 2:
            for value in values:
                if (value >> keys[bit]) & 1 == 1:
                    new_values.append(value)
        else:
            for value in values:
                if (value >> keys[bit]) & 1 == 0:
                    new_values.append(value)
        bit += 1
        return (
            new_values
            if bit >= len(keys) or len(new_values) == 1
            else self.get_oxygen_reading(new_values, bit)
        )

    def search_carbon_reading(self):
        values = self._history.copy()
        return self.get_carbon_reading(values, 0)

    def get_carbon_reading(self, values, bit):
        sub_diag = Diagnostic()
        new_values = []
        keys = sorted(self.ones.keys(), reverse=True)
        for value in values:
            sub_diag.analyze(value)
        zeros = len(sub_diag._history) - sub_diag.ones[keys[bit]]
        if zeros <= (len(sub_diag._history) / 2):
            for value in values:
                if (value >> keys[bit]) & 1 != 1:
                    # print(f"({bin(value)} >> {keys[bit]} ^ 0) == 1")
                    new_values.append(value)
        else:
            for value in values:
                if (value >> keys[bit]) & 1 != 0:
                    # print(f"({bin(value)} >> {keys[bit]} ^ 0) == 0")
                    new_values.append(value)
        bit += 1
        # print(bit)
        # print(values)
        return (
            new_values
            if bit >= len(keys) or len(new_values) == 1
            else self.get_carbon_reading(new_values, bit)
        )
