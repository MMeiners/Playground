#!/usr/bin/env python3
"""
Date   : 2020-10-01
Purpose: Mad libs
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Mad libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='input',
                        type=str,
                        nargs='*',
                        default=None)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()
    substitutions = args.inputs
    text = args.file.read().strip()
    args.file.close()

    placeholders = re.findall(r"(<([^<>]+)>)", text)

    if not placeholders:
        sys.exit(f'"{args.file.name}" has no placeholders.')

    for _, holder_name in placeholders:

        if not substitutions:
            a_an = 'an' if holder_name[0] in 'aeiou' else 'a'
            user_choice = input(f"Give me {a_an} {holder_name}: ")
        else:
            user_choice = substitutions.pop(0)

        text = re.sub(r"(<([^<>]+)>)", user_choice, text, count=1)

    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
