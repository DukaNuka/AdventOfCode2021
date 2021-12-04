class InputReader:
    @staticmethod
    def read_file_to_function(filename: str, function, ignore_first: bool = False):
        i = 0
        with open(filename, "r") as infile:
            if ignore_first:
                infile.readline()
            for line in infile.readlines():
                function(line.strip())
                i += 1
        print(f"Analyzed {i} lines")
