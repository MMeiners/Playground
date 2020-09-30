#!/usr/bin/env python3
"""
Date   : 2020-09-29
Purpose: Southern fry text
"""

import argparse
import re
import os


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
def fry_word(word: str) -> str:
    if re.match(r"[Yy]ou$", word):
        return word[0] + "'all"

    word_group = re.search(r"(.+)ing$", word)

    if word_group and re.search(r"[aeiouy]", word_group.group(1).lower()):
        return word_group.group(1) + "in'"
    else:
        return word


# --------------------------------------------------
def test_fry_word():
    assert fry_word('you') == "y'all"
    assert fry_word('You') == "Y'all"
    assert fry_word('fishing') == "fishin'"
    assert fry_word('Aching') == "Achin'"
    assert fry_word('swing') == "swing"


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()
    all_lines = []

    if os.path.isfile(args.text):
        with open(args.text) as file:
            all_lines.extend(file.readlines())
    else:
        all_lines.append(args.text)

    for line in all_lines:
        split_line = re.split(r"(\W)", line)
        fried_words = map(fry_word, split_line)
        print(''.join(fried_words), end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
