#!/usr/bin/env python3
"""
Date   : 2020-09-23
Purpose: You said, but I heard...
"""

import argparse
import random
import os
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
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

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=.1)

    args = parser.parse_args()

    if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        with open(args.text, encoding='utf-8') as file:
            args.text = file.read()

    return args


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()
    text = args.text.rstrip()
    scrambled = text
    random.seed(args.seed)
    length = len(text)

    num_mutations = round(length * args.mutations)
    new_chars = ''.join(sorted(string.ascii_letters + string.punctuation))
    indexes_to_swap = random.sample(range(length), num_mutations)

    for index in indexes_to_swap:
        new_char = random.choice(new_chars.replace(scrambled[index], ''))
        scrambled = scrambled[:index] + new_char + scrambled[index+1:]

    print(f'You said: "{text}"')
    print(f'I heard : "{scrambled}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
