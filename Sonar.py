class Sonar:
    def __init__(self):
        self._depth = None
        self._deeper = 0
        self._shallower = 0
        self._depth_sum = 0
        self._sum_deeper = 0
        self._sum_shallower = 0
        self._last_deeper = None
        self._history = []

    @property
    def sum_deeper( self ):
        return self._sum_deeper

    @property
    def sum_shallower( self ):
        return self._sum_shallower

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
    def depth( self, new_depth ):
        self.compare_sums( new_depth )
        if self._depth is None:
            self._depth = new_depth
        elif new_depth > self._depth:
            self._deeper += 1
            self._last_deeper = True
        elif new_depth < self._depth:
            self._shallower += 1
            self._last_deeper = False
        self._depth = new_depth
        self.history.append( new_depth )
        self._depth_sum = sum(self.history[-3:])

    def compare_sums( self, new_depth ):
        if len(self.history) > 2:
            if sum(self.history[-2:]) + new_depth > sum(self.history[-3:]):
                self._sum_deeper+=1
            else:
                self._sum_shallower+=1

    def analyze_new_depth( self, new_depth ):
        self.depth = int(new_depth)