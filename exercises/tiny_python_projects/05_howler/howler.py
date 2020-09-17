#!/usr/bin/env python3
"""
Date   : 2020-09-17
Purpose: Howler message writer
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Howlers by owl',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('message',
                        metavar='text',
                        help='Text to howl')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=argparse.FileType('wt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()
    message = str(args.message)

    with (args.outfile if args.outfile else sys.stdout) as output:
        if os.path.isfile(message):
            with open(message, encoding='utf-8') as read_in:
                for line in read_in:
                    print(line.upper(), file=output, end='')
        else:
            print(message.upper(), file=output)


# --------------------------------------------------
if __name__ == '__main__':
    main()
