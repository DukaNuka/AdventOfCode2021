class Submarine:
    def __init__(self):
        self._current_depth = 0
        self._current_latitude = 0
        self._aim = 0

    @property
    def current_depth(self):
        return self._current_depth

    @property
    def latitude(self):
        return self._current_latitude

    def move(self, command, value):
        MOVE_FUNCTIONS = {
            "forward": self.move_forward,
            "up": self.move_up,
            "down": self.move_down,
        }
        MOVE_FUNCTIONS[command](value)

    def parse_line(self, line):
        line_content = line.split(" ")
        command = str(line_content[0].strip())
        value = int(line_content[1].strip())
        self.move(command, value)

    def move_down(self, value):
        self._current_depth += value

    def move_up(self, value):
        self._current_depth -= value

    def move_forward(self, value):
        self._current_latitude += value

    def move_back(self, value):
        self._current_latitude -= value
