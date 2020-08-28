# Problem: write a function that takes a string of numbers and sums them using a generator
# Input: user entered string of numbers
# Output: sum of numbers int


def sum_numbers(user_input: str) -> int:
    """ from the input string, return the sum """

    list_of_numbers = (int(number) for number in user_input.split() if number.isdigit())
    total = sum(list_of_numbers)

    return total


while True:
    number_string = input('Please enter a series of integers: ')

    if not number_string:
        print('Nothing to sum!')
        break

    print(f'The sum is: {sum_numbers(number_string)}')
