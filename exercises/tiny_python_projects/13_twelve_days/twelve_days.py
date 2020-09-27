#!/usr/bin/env python3
"""
Date   : 2020-09-26
Purpose: Twelve days of Christmas song
"""

import argparse
import sys

ORDINAL_DAY = ['no zeroth day', 'first', 'second', 'third', 'fourth', 'fifth',
               'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh',
               'twelfth', 'thirteenth']

GIFTS = """padding, A partridge in a pear tree, Two turtle doves,
Three French hens, Four calling birds, Five gold rings, Six geese a laying,
Seven swans a swimming, Eight maids a milking, Nine ladies dancing,
Ten lords a leaping, Eleven pipers piping,
Twelve drummers drumming""".split(',')


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    # I'm not sure I would do this in production, it doesn't handle closing
    # the handle it opens here automatically from what I've seen.
    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt', encoding='utf-8'),
                        default=sys.stdout)

    args = parser.parse_args()

    if args.num < 1 or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def sing_verse(day):
    """ Sing a verse for given day """

    and_a = "A" if day == 1 else "And a"

    verse_lines = [f'On the {ORDINAL_DAY[day]} day of Christmas',
                   'My true love gave to me']
    verse_lines.extend([GIFTS[day].strip() for day in range(day, 1, -1)])
    verse_lines.append(f'{and_a} partridge in a pear tree.')

    return ',\n'.join(verse_lines)


# --------------------------------------------------
def test_sing_verse():
    """ Test sing verse """
    assert sing_verse(1) == '\n'.join(['On the first day of Christmas,',
                                       'My true love gave to me,',
                                       'A partridge in a pear tree.'])

    assert sing_verse(2) == '\n'.join(['On the second day of Christmas,',
                                       'My true love gave to me,',
                                       'Two turtle doves,',
                                       'And a partridge in a pear tree.'])


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()
    whole_song = []

    for day in range(1, args.num + 1):
        whole_song.append(sing_verse(day))

    print('\n\n'.join(whole_song), file=args.outfile)
    args.outfile.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
