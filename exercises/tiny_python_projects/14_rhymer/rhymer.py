#!/usr/bin/env python3
"""
Date   : 2020-09-27
Purpose: Let's rhyme
"""

import argparse
import re
import string


consonants_list = [char for char in string.ascii_lowercase
                   if char not in 'aeiou']
rhyme_list = """bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st
sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr""".split(' ')

NEW_PREFIX = rhyme_list + consonants_list
CONSONANTS = ''.join(consonants_list)


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
def split_word(word: str) -> tuple:
    """ Return any leading consonants and remainder of the word"""
    match = re.match(f'([{CONSONANTS}]+)?([aeiou])(.*)', word.lower())

    if match:
        group1 = match.group(1) or ''
        group2 = match.group(2) or ''
        group3 = match.group(3) or ''
    else:
        group1, group2, group3 = word.lower(), '', ''

    return group1, group2 + group3


# --------------------------------------------------
def test_split_word():
    """ Test split_word for valid IO """

    assert split_word('') == ('', '')
    assert split_word('cake') == ('c', 'ake')
    assert split_word('chair') == ('ch', 'air')
    assert split_word('APPLE') == ('', 'apple')
    assert split_word('RDNZL') == ('rdnzl', '')
    assert split_word('123') == ('123', '')


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()

    word_parts = split_word(args.word)

    if word_parts[1] == '':
        print(f'Cannot rhyme "{args.word}"')
    else:
        rhymes = [prefix + word_parts[1] for prefix in NEW_PREFIX
                  if prefix != word_parts[0]]
        rhymes = '\n'.join(sorted(rhymes))
        print(rhymes)


# --------------------------------------------------
if __name__ == '__main__':
    main()
