# Problem: we want to know the number of unique numbers in a list
# Input: a list of numbers
# Output: total unique count

def get_unique_count(list_of_numbers: list) -> int:
    """ Get the count of unique numbers in the list """

    set_of_numbers = set()

    for item in list_of_numbers:
        try:
            set_of_numbers.add(int(item))
        except (ValueError, TypeError):
            continue

    return len(set_of_numbers)


print(get_unique_count([1, 2, 3]))
print(get_unique_count([1, 2, 2]))
print(get_unique_count([1, 'a', 3]))
print(get_unique_count([1.0, 2, 2.0]))
print(get_unique_count([1, 1.0, 1.05]))
print(get_unique_count([0, 0.0, 0.05]))
