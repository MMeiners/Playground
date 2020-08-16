# Problem: take a customer's lunch order and give them a total
# Input: string values until blank line entered
# Output: confirmation/denial of item ordered and the total bill

import collections


LUNCH_MENU = {'salad': 10,
              'sandwich': 8,
              'soup': 5,
              'tea': 3,
              'soda': 4,
              'daily special': 15,
              'water': 2}


def take_lunch_order():
    """ Ask the customer for their lunch order and bring the tab """

    total_tab = 0
    lunch_order = collections.Counter()

    print_menu()

    while True:
        order = str(input('Enter item to order, menu, or leave blank to finish: ')).strip().lower()

        if not order:
            break
        elif order == 'menu':
            print_menu()
        elif order not in LUNCH_MENU:
            print('Only items on the menu please, 1 at a time.')
        else:
            lunch_order.update([order])
            total_tab += LUNCH_MENU[order]
            print(f'{order.capitalize()} costs ${LUNCH_MENU[order]}, your total so far is ${total_tab}')

    if total_tab > 0:
        print(f'Your total today is: ${total_tab}')
        print(f'Have a nice day!')
    else:
        print(f'Let me know when you are ready to order.')


def print_menu():
    print("Today's Lunch Menu")
    print("------------------")

    for key, value in LUNCH_MENU.items():
        print(f'{key.capitalize()}, ${value}')

    print('')


take_lunch_order()
