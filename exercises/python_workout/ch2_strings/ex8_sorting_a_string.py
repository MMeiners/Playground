# Problem: simple, sort an input string.  Seems much easier than the last few exercises.
# Input: string to sort
# Output: sorted string

def string_sort(some_string):
    """ Sort the input string. """

    try:
        some_string = str(some_string)

        return ''.join(sorted(some_string))
    except (ValueError, TypeError):
        return 'Unexpected value detected'


print(string_sort('bac'))
print(string_sort('test'))

# Ha, lots of special cases in this one.  Maybe fix?  Book didn't call for it.
print(string_sort('This is a test!'))
