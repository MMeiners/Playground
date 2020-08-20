# Problem: read a unix style password file and return a dict based on it
# Input: filename string
# Output: processed dict object (key=username, value=user id)

import pprint


def convert_passwd_to_dict(filename: str) -> dict:
    """ Convert the password file given to a dict with usernames and id values"""

    users_dict = {}

    try:
        with open(filename) as file:
            for line in file:
                if not line.startswith(('#', '\n')):
                    user_data = line.strip().split(':')
                    users_dict[user_data[0]] = user_data[2]

        return users_dict
    except (ValueError, TypeError):
        return {}


# since we are printing a large dict, use data pretty printer instead of the normal print()
pprint.pp(convert_passwd_to_dict('passwd.txt'))
