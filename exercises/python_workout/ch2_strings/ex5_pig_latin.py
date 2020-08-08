# Problem: write a function that takes a string as an english word and applies a pig latin transformation
# Input: string
# Output: pig latin translated form of input string

def pig_latin(word):
    """Transform string using pig latin rules"""

    try:
        word = str(word)

        if not word.isalpha():
            raise ValueError

        if word[0] in 'aeiou':
            transformed_word = f'{word}way'
        else:
            transformed_word = f'{word[1:]}{word[0]}ay'

        return transformed_word
    except (TypeError, ValueError):
        return 'Not a valid word'


""" really need to start using pytest on these exercises...
print(pig_latin('apple'))
print(pig_latin('python'))
print(pig_latin('apple123'))
print(pig_latin('123'))
print(pig_latin(['a']))
"""