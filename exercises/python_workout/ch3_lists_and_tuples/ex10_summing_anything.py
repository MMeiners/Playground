# Problem: sum the arguments passed and return as an object of the same type
# Input: variable number of sequence objects (eg string, list, tuple)
# Output: sum of the arguments in the correct type (eg list returns a list)

def sum_items(*items):
    """ Sum the items"""

    try:
        if not items:
            return items

        # Without testing arg types, this line initializes the output type correctly and assigned it a value.
        # This has implications for the for loop needing a slice to skip over element 0
        summed_up = items[0]

        for item in items[1:]:
            summed_up += item

        return summed_up
    except (ValueError, TypeError):
        return 'Unexpected item encountered'


print(sum_items(1, 2, 3))
print(sum_items([1, 2], [3], [4, 5]))
print(sum_items('a', 'b', 'c'))
print(sum_items({1, 2}, {3}))
