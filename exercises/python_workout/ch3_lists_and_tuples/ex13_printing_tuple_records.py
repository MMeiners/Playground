# Problem: transform an input list of tuples and format them to spec
# Input: list of tuples
# Output: transformed tuples where names are in 10 char fields, time in 5 char fields displayed to 2 decimals

import operator


PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]


def format_sort_records(guest_list):
    """ Print out the records in the proper format and sort """

    format_template = '{1:10} {0:10} {2:5.2f}'

    for person in sorted(guest_list, key=operator.itemgetter(1, 0)):
        print(format_template.format(*person))


format_sort_records(PEOPLE)
