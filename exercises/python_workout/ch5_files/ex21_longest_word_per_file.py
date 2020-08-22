# Problem: write two functions.  One takes a filename and returns the longest word.  The second function takes
#          a directory argument, then returns a dict where the keys are filenames and values are the longest word
# Input: filename string and directory string
# Output: either the longest word or a dict mapping longest words to their filename

import os
import pprint


def find_longest_word(filename: str) -> str:
    """ Find the longest word in the given file """

    longest_word = ''

    try:
        with open(filename, encoding='utf-8') as file:  # big oof here... windows was defaulting cp1252 and crashing
            for line in file:
                for word in line.strip().split():
                    if len(word) > len(longest_word):
                        longest_word = word

        return longest_word
    except (ValueError, TypeError):
        return 'Error'


def find_all_longest_words(directory: str) -> dict:
    """ For each file in the directory, get the longest word """

    # we could use a dict comprehension here but those are chapter 7  >.<  ;)

    longest_words = {}

    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)

        if os.path.isfile(filepath):
            longest_words[file] = find_longest_word(filepath)

    return longest_words


pprint.pp(find_all_longest_words('ebooks'))
