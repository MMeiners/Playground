#!/usr/bin/env python3
"""
Date   : 2020-09-30
Purpose: Scramble the letters of words
"""

import argparse
import random
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
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
def scramble(word: str) -> str:
    """ scramble the word! """

    if len(word) > 3 and re.match(r"[a-zA-Z]+", word):
        first_letter = list(word[0])
        last_letter = list(word[-1])
        middle_letters = list(word[1:-1])

        random.shuffle(middle_letters)

        return ''.join(first_letter + middle_letters + last_letter)
    else:
        return word


# --------------------------------------------------
def test_scramble():
    """ test scramble function """
    random_state = random.getstate()
    random.seed(1)

    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"

    random.setstate(random_state)


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()
    random.seed(args.seed)
    regex_splitter = re.compile(r"([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")

    for line in args.text.splitlines():
        split_line = regex_splitter.split(line)
        print(''.join(map(scramble, split_line)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
