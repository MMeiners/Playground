#!/usr/bin/env python3
"""
Date   : 2020-09-24
Purpose: Sing bottles of beer song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def sing_verse(bottle_count: int) -> str:
    """ Sing a verse """

    s = "s" if bottle_count > 1 else ""
    last_s = "" if bottle_count == 2 else "s"
    last_call = "No more" if bottle_count == 1 else f"{bottle_count-1}"

    return '\n'.join([f'{bottle_count} bottle{s} of beer on the wall,',
                      f'{bottle_count} bottle{s} of beer,',
                      'Take one down, pass it around,',
                      f'{last_call} bottle{last_s} of beer on the wall!'])


# --------------------------------------------------
def test_verse():
    """ Test verses """

    last_verse = sing_verse(1)
    assert last_verse == '\n'.join(['1 bottle of beer on the wall,',
                                    '1 bottle of beer,',
                                    'Take one down, pass it around,',
                                    'No more bottles of beer on the wall!'])

    two_bottles = sing_verse(2)
    assert two_bottles == '\n'.join(['2 bottles of beer on the wall,',
                                     '2 bottles of beer,',
                                     'Take one down, pass it around,',
                                     '1 bottle of beer on the wall!'])


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()

    for verse_number in range(args.num, 0, -1):
        print(sing_verse(verse_number))
        if verse_number > 1:
            print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
