#!/usr/bin/env python3
"""
Date   : 2020-10-01
Purpose: Mad libs
"""

import argparse


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


# --------------------------------------------------
if __name__ == '__main__':
    main()
