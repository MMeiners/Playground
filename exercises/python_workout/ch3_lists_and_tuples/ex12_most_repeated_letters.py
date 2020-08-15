# Problem: return the word with the most repeated characters
# Input: sequence of strings
# Output: string which has the most repeated letters

from collections import Counter

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']


def get_string_most_repeated_letters(string_list):
    """ Get the string with the highest number of repeated letters"""
    return max(string_list, key=get_letter_counts)


def get_letter_counts(word):
    """ Get the highest repeated letter count for use in key functions. """

    most_common_letter = Counter(word).most_common(1)[0]    # get the first tuple from the most_common list obj
    letter_count = most_common_letter[1]

    return letter_count


print(get_string_most_repeated_letters(WORDS))
