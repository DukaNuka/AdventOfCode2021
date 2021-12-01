class Sonar(object):
    def __init__(self):
        self._depth = None
        self._deeper = 0
        self._shallower = 0
        self._last_deeper = None
        self._history = []

    @property
    def deeper(self):
        return self._deeper

    @property
    def shallower(self):
        return self._shallower

    @property
    def last_deeper(self):
        return self._last_deeper

    @property
    def history(self):
        return self._history

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self.history.append(value)
        if self._depth is None:
            self._depth = value
        elif value > self._depth:
            self._deeper += 1
            self._last_deeper = True
        elif value < self._depth:
            self._shallower += 1
            self._last_deeper = False
        self._depth = value

    def analyze_new_depth( self, new_depth ):
        self.depth = int(new_depth)