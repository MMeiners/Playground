#!/usr/bin/env python3
"""
Date   : 2020-09-21
Purpose: Random insults
"""

import argparse
import random

ADJECTIVES = """bankrupt base caterwauling corrupt cullionly 
detestable dishonest false filthsome filthy foolish foul gross heedless 
indistinguishable infected insatiate irksome lascivious lecherous 
loathsome lubbery old peevish rascaly rotten ruinous scurilous scurvy 
slanderous sodden-witted thin-faced toad-spotted unmannered vile 
wall-eyed""".split()

NOUNS = """Judas Satan ape ass barbermonger beggar block boy braggart butt 
carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool gull 
harpy jack jolthead knave liar lunatic maw milksop minion ratcatcher 
recreant rogue scold slave swine traitor varlet villain worm""".split()


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2)

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='insults',
                        type=int,
                        default=3)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """ Start here """

    args = get_args()
    random.seed(args.seed)
    number_adjectives = args.adjectives
    number_insults = args.number

    for _ in range(number_insults):
        colorful_adjectives = random.sample(ADJECTIVES, number_adjectives)
        insulting_name = random.choice(NOUNS)
        print(f'You {", ".join(colorful_adjectives)} {insulting_name}!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
