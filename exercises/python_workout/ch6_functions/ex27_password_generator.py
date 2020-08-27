# Problem: create a password generator function which returns a function accepting a password length based on the
#          allowable characters passed to the generator.
# Input: a string of valid password characters and a length of desired password
# Output: a random password string

import random
from typing import Callable


def create_password_generator(valid_characters: str) -> Callable[[int], str]:
    """ Create a function to generate a password based on the valid characters"""

    def create_password(password_length: int) -> str:
        """ Create random password of length """

        password = ''

        for _ in range(password_length):
            password += random.choice(valid_characters)

        return password

    return create_password


alpha_password = create_password_generator('abc')
mixed_password = create_password_generator('abc123!@#')
print(alpha_password(5))
print(alpha_password(10))
print(mixed_password(5))
print(mixed_password(10))
