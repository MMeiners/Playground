#!/usr/bin/env python3
"""
Date   : 2020-09-27
Purpose: Let's rhyme
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()


# --------------------------------------------------
if __name__ == '__main__':
    main()
