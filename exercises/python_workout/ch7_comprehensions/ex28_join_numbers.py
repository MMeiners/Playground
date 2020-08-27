# Problem: given a range of ints, return a csv string of the ints
# Input: sequence of int values
# Output: csv string

import typing


def join_numbers(some_numbers: typing.Sequence) -> str:
    """ Create a csv string from the input numbers """

    string_list = [str(number) for number in some_numbers]

    return ','.join(string_list)


print(join_numbers(range(20)))
