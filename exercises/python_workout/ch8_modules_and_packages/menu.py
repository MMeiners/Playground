# Problem: create a function that takes named arguments where the named argument is called if it matches the user input
# Input: function arguments, user input
# Output: whatever the corresponding function outputs... for this exercise let's go with a simple string

from typing import Callable


def menu(**kwargs: Callable) -> str:
    """ ask the user for their choice and execute it """

    print('Menu Options')
    for key in kwargs:
        print(key)

    while True:
        choice = input('Please enter your choice: ')

        if choice not in kwargs:
            print('That option is not available, please try again')
            continue
        else:
            return kwargs[choice]()
