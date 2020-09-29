#!/usr/bin/env python3
"""
Date   : 2020-09-29
Purpose: Southern fry text
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()


# --------------------------------------------------
if __name__ == '__main__':
    main()
