#!/usr/bin/env python3
"""
Date   : 2020-09-25
Purpose: Ransom Note
"""

import argparse
import random
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text) as file:
            args.text = file.read()

    return args


# --------------------------------------------------
def choose(char):
    """ Decide if the char should be upper or lowercase """
    return char.lower() if random.choice([True, False]) else char.upper()


# --------------------------------------------------
def test_choose():
    """ test choose() """
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state)


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()
    random.seed(args.seed)
    ransom_note = ''.join(map(choose, args.text))
    print(ransom_note)


# --------------------------------------------------
if __name__ == '__main__':
    main()
