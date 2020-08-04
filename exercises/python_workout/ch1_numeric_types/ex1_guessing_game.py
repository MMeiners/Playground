# Problem: create a function that compares a user input to a random number in [0,100] and lets the user know if they
# are high, low, or correct.  Exit upon successful guess.

import random


def guessing_game():
    correct_answer = random.randint(0, 100)

    print('Please guess a number between 0 and 100 inclusive.\n')

    while True:
        try:
            user_guess = int(input('Your number please: '))
        except ValueError:
            print("Hmm, whole numbers only please.  Try again.\n")
            continue

        if user_guess < correct_answer:
            print("I'm sorry, that's too low.\n")
        elif user_guess > correct_answer:
            print("I'm sorry, that's too high.\n")
        elif user_guess == correct_answer:
            print(f"Correct!  I was thinking {correct_answer}!")
            break


guessing_game()
