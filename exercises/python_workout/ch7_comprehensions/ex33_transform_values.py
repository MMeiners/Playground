# Problem: create a variation on map() where it takes a function and a dict, returning the transformed dict
# Input: function to map and a dict
# Output: transformed dict

from typing import Callable
from typing import Any


def transform_values(user_func: Callable[[Any], Any], original: dict) -> dict:
    """ Transform values using supplied function """

    return {key: user_func(value) for key, value in original.items()}


double_me = {'One': 1,
             'Two': 2,
             'Three': 3,
             'Four': 4,
             'Five': 5}

print(transform_values(lambda x: x * 2, double_me))
