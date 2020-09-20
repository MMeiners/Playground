#!/usr/bin/env python3
"""
Date   : 2020-09-20
Purpose: Substitute vowels from input with a new vowel
"""

import argparse
import os

VOWELS = 'aeiouAEIOU'


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Apples and Bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        choices=['a', 'e', 'i', 'o', 'u'],
                        default='a')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()
    new_vowel = args.vowel.lower()
    text = args.text

    vowel_mappings = {vowel: new_vowel if vowel.islower() else new_vowel.upper()
                      for vowel in VOWELS}
    translator = str.maketrans(vowel_mappings)

    if os.path.isfile(text):
        with open(text, encoding='utf-8') as file:
            for line in file:
                print(line.translate(translator), end='')
    else:
        print(text.translate(translator))


# --------------------------------------------------
if __name__ == '__main__':
    main()
