# Problem: transform strings from one file and write to a second.  Transform is a basic reverse
# Input: two input filename strings
# Output: reversed lines written to disk

import pathlib


def reverse_lines(read_file: str, write_file: str) -> None:
    """ Reverse the lines found in the read_file and write them out """

    source_path = pathlib.Path(read_file)
    output_path = pathlib.Path(write_file)

    with open(source_path) as source, open(output_path, 'w') as output:
        for line in source.readlines():
            output.write(line.rstrip()[::-1] + '\n')


reverse_lines('test_file.txt', 'test_reversed.txt')
