# Problem: extend the previous pig latin exercise to work with a sentence.  For this, we will assume no punctuation
# and ignore capitalization for simplicity sake.
# Input: sentence string
# Output: sentence transformed using pig latin rules

from ex5_pig_latin import pig_latin


def pig_latin_sentence(sentence):
    """Transform words in a string to pig latin"""

    try:
        sentence = str(sentence)

        words_to_transform = sentence.split()
        transformed_words = []

        for word in words_to_transform:
            transformed_words.append(pig_latin(word))

        return ' '.join(transformed_words)
    except (ValueError, TypeError):
        return 'Unexpected value found'


print(pig_latin_sentence('why hello there'))
