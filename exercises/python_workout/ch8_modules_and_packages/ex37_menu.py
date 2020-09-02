# Problem: import the menu and ask the user to pick a function to run
# Input: user input to the imported menu
# Output: string output from selected function

from menu import menu


def hello():
    return 'Hello'


def world():
    return 'World'


def wrong_door():
    return 'Nobody home!'


print(menu(a=hello, b=world, c=wrong_door))
