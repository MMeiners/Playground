#!/usr/bin/env python3
"""
Date   : 2020-09-15
Purpose: Print what you are bringing to the picnic!
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Item(s) to bring',
                        nargs='+')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()
    food_list = args.str
    number_of_items = len(food_list)

    if args.sorted:
        food_list.sort()

    if number_of_items == 1:
        food_expected = food_list[0]
    elif number_of_items == 2:
        food_expected = f'{food_list[0]} and {food_list[1]}'
    else:
        food_expected = f'{", ".join(food_list[:-1])}, and {food_list[-1]}'

    print(f'You are bringing {food_expected}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
