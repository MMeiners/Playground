#!/usr/bin/env python3
"""
Date   : 2020-09-16
Purpose: Jump the five
"""

import argparse

JUMP_MAP = {'1': '9', '2': '8', '3': '7',
            '4': '6', '5': '0', '6': '4',
            '7': '3', '8': '2', '9': '1',
            '0': '5'}


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('plain_text',
                        metavar='str',
                        help='Input text',
                        nargs='+')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()
    plain_text = ' '.join(args.plain_text)

    encoded_list = [JUMP_MAP.get(letter, letter)
                    for letter in plain_text]

    print(''.join(encoded_list))


# --------------------------------------------------
if __name__ == '__main__':
    main()
