# Problem: given a dict, flip the key:value pairs around using a comprehension.  eg usernames swap user ids.
#          This obviously assumes the values being switched into keys are unique as well.
# Input: dict
# Output: dict with the key value pairs role reversed.


def flip_dict(input_dict: dict) -> dict:
    """ Flip the key:value pairs around """

    return {value: key for key, value in input_dict.items()}


users = {'Luke': 1,
         'Leia': 2,
         'Han': 3,
         'Yoda': 4}

print(flip_dict(users))
