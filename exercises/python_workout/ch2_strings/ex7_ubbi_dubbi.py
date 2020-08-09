# Problem: take a string as a word, and apply ubbi dubbi transformation to it (add ub before each vowel).
# Input: string word
# Output: transformed string word

def ubbi_dubbi(word):
    transformation_buffer = []

    try:
        word = str(word)

        for letter in word:
            if letter in 'aeiou':
                transformation_buffer.append('ub')

            transformation_buffer.append(letter)

        return ''.join(transformation_buffer)
    except (TypeError, ValueError):
        return 'Unknown value found'


print(ubbi_dubbi('test'))
print(ubbi_dubbi('banana'))
print(ubbi_dubbi('milk'))
