# Problem: using list comprehensions flatten a list of lists 1 deep
# Input: a list of lists eg [[1, 2], [3, 4]]
# Output: list eg [1, 2, 3, 4]

def flatten(some_list: list) -> list:
    """ Flatten a list of lists """

    return [item for inner_list in some_list for item in inner_list]


print(flatten([[1, 2], [3, 4], [5, 6, 7]]))
