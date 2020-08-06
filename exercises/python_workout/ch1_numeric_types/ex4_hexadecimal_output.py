# Problem: write a function that takes a hex number and returns an int
# Input: hex number (eg 0x50)
# Output: hex converted to int (eg 80)

def hex_to_int():
    """Convert hex to int"""

    return_value = 0
    user_input = input('Enter a hex number to convert to int (eg 0x50): ')

    if user_input[0:2] == '0x':
        # reversed_numbers = user_input[-1:1:-1]    # cleaner but harder to *grasp*
        reversed_numbers = reversed(user_input[2:])

        for position, number in enumerate(reversed_numbers):
            try:
                return_value += int(number, 16) * (16 ** position)
            except ValueError:
                print(f'Unexpected character found: {number}, expect hex characters 0-9 and a-f')
                return_value = None
                break

        if return_value is not None:
            print(return_value)
    else:
        print('Input not in expected format.  Expected 0x followed by numbers/characters')


hex_to_int()
