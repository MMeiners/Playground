#!/usr/bin/env python3
"""
Date   : 2020-09-14
Purpose: On the lookout for the captain!
"""

import argparse

VOWELS = 'aeiou'


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='What did we find?')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()
    word = args.word
    first_letter = word[0].lower()

    article = 'an' if first_letter in VOWELS else 'a'

    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
