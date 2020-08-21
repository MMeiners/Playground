# Problem: write two functions.  One takes a filename and returns the longest word.  The second function takes
#          a directory argument, then returns a dict where the keys are filenames and values are the longest word
# Input: filename string and directory string
# Output: either the longest word or a dict mapping longest words to their filename

import os


def find_longest_word(filename: str) -> str:
    """ Find the longest word in the given file """
    longest_word = ''
    line_count = 0

    try:
        with open(filename, encoding='utf-8') as file:  # big oof here... windows was defaulting cp1252 and crashing
            for line in file:
                line_count += 1
                for word in line.strip().split():
                    if len(word) > len(longest_word):
                        longest_word = word
        return longest_word
    except (ValueError, TypeError):
        return ''


def find_all_longest_words(directory: str) -> dict:
    """ to be implemented """
    pass


print(find_longest_word('ebooks\\43-0.txt'))
