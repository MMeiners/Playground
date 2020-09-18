#!/usr/bin/env python3
"""
Date   : 2020-09-18
Purpose: write a python version of wc
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt', encoding='utf-8'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()

    total_lines, total_words, total_bytes = 0, 0, 0

    for each_file in args.input_file:
        file_lines, file_words, file_bytes = 0, 0, 0

        for each_line in each_file:
            file_lines += 1
            file_bytes += len(each_line)
            file_words += len(each_line.split())

        total_lines += file_lines
        total_words += file_words
        total_bytes += file_bytes

        print(f'{file_lines:8}{file_words:8}{file_bytes:8} {each_file.name}')

    if len(args.input_file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_bytes:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
