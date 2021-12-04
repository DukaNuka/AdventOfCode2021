class InputReader:
    @staticmethod
    def read_file_to_function(
        filename: str, function, ignore_first: bool = False, special_first=None
    ):
        i = 0
        with open(filename, "r") as infile:
            if ignore_first:
                if special_first is not None:
                    special_first(infile.readline().strip())
                else:
                    infile.readline()
            for line in infile.readlines():
                function(line.strip())
                i += 1
        print(f"Analyzed {i} lines")
