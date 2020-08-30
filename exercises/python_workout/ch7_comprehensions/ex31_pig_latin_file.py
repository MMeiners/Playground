# Problem: translate a file into pig latin and return the new string
# Input: a text file and file location
# Output: translated string value

from ex5_pig_latin import pig_latin as pig


def make_pig_latin(filename: str) -> str:
    """ Translate the file into pig latin """

    with open(filename) as file:

        translator = (pig(word) for line in file for word in line.split() if pig(word) != 'Not a valid word')

        translation = ' '.join(translator)

    return translation


print(make_pig_latin('..\\ch5_files\\wcfile.txt'))
