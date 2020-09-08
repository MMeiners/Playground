# Problem: create a generator function that returns lines from each file in a directory.  I'm going to limit
#          to just txt files in the ch5 directory for now.
# Input: directory string
# Output: line strings

import pathlib


def get_all_lines(directory: str) -> str:
    """ Read all the lines in each text file in the directory """

    try:
        directory_path = pathlib.Path(directory)

        for each_path in directory_path.glob('*.txt'):
            with open(str(each_path)) as each_file:
                for each_line in each_file:
                    yield each_line
    except (OSError, ValueError, TypeError):
        pass


if __name__ == '__main__':
    for line in get_all_lines('..\\ch5_files'):
        print(line.strip())
