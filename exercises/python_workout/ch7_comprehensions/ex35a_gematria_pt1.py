# Problem: using a dict comprehension, create a dict where the keys are letters in the alphabet and values are the
#          corresponding ordered position
# Input: none
# Output: dict

from string import ascii_lowercase


def get_gematria() -> dict:
    """ Generate gematria dict """

    return {char: index for index, char in enumerate(ascii_lowercase, 1)}


print(get_gematria())
