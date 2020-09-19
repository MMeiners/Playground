#!/usr/bin/env python3
"""
Date   : 2020-09-19
Purpose: Gashlycrumb
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='str',
                        type=str,
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()
    text_lookup = {}

    if os.path.isfile(args.file):
        with open(args.file) as read_from:
            for line in read_from:
                text_lookup[line[0].lower()] = line
    else:
        sys.exit(f"No such file or directory: '{args.file}'")

    for letter in args.letter:
        if letter.lower() in text_lookup:
            print(text_lookup[letter.lower()], end='')
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
