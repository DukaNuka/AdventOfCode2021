from Sonar import Sonar
from InputReader import InputReader

if __name__ == '__main__':
    print('main')
    sonar = Sonar()
    InputReader.read_file_to_function("SonarInput.txt", sonar.analyze_new_depth)
