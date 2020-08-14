# Problem: assuming a list of dictionaries representing a contact list, sort by last name then first name
# Input: none, assume a 'const' variable defined outside the function exists for this exercise
# Output: a list sorted by the last name and first name

import operator

CONTACT_LIST = [
    {'first_name': 'Agent', 'last_name': 'Smith', 'location': 'The Matrix Simulation'},
    {'first_name': 'Thomas', 'last_name': 'Anderson', 'location': 'Zion'},
    {'first_name': 'Luke', 'last_name': 'Skywalker', 'location': 'Tatooine'},
    {'first_name': 'Leia', 'last_name': 'Skywalker', 'location': '<Top Secret>'}
]


def alphabetize_names():
    """ Print sorted contacts using itemgetter """
    sort_columns = operator.itemgetter('last_name', 'first_name')

    for contact in sorted(CONTACT_LIST, key=sort_columns):
        print(f'{contact["last_name"]}, {contact["first_name"]} can be found at {contact["location"]}')


def alphabetize_names_lambda():
    """ Print sorted contacts using a lambda instead """

    for contact in sorted(CONTACT_LIST, key=lambda entry_item: (entry_item['last_name'], entry_item['first_name'])):
        print(f'{contact["last_name"]}, {contact["first_name"]} can be found at {contact["location"]}')


alphabetize_names()
print('--------------------------------------------------------------')
alphabetize_names_lambda()
