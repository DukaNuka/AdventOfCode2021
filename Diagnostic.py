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
