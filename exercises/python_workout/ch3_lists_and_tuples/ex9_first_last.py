# Problem: return the first and last object from a sequence
# Input: a sequence like a string or list
# Output: the first and last items from the sequence in the same format as the input (eg given a list, return a list)


def get_first_last(input_sequence):
    """ Get the first and last items from the sequence"""

    try:
        return input_sequence[:1] + input_sequence[-1:]
    except (ValueError, TypeError):
        return 'Something not quite right here...'


print(get_first_last([1, 2, 3, 4]))
print(get_first_last('apple'))
print(get_first_last({'my', 'set', 'object'}))
