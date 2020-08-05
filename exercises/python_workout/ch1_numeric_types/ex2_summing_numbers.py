# Problem: reimplement the standard sum() function minus the optional second argument.
# Function input: variable amount of numeric arguments.  (Unlike the standard sum() which takes an iterable.)
# Function output: sum of the inputs

def sum_numbers(*numbers):
    """Return the sum of a variable number of whole numbers"""

    result = 0

    for number in numbers:
        try:
            result += int(number)
        except (ValueError, TypeError) as error_instance:
            # If the arg isn't a number, what should we do?  Skip?
            print(f'Argument not a number: {number}, {error_instance.args}')
            continue

    return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(1, 'a', 3))
print(sum_numbers(1, 2, [3, 4]))
print(sum_numbers(1, 0.5))
print(sum_numbers(*[1, 2, 3]))
