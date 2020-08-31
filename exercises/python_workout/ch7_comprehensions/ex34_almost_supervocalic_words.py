# Problem: given a text file of words, find all words that contain at least one of each vowel (a, e, i, o, u)
# Input: filename string
# Output: a set of strings meeting the criteria above


def get_vocalic(filename: str) -> set:
    """ Find the words with every vowel in them """

    vowels = {'a', 'e', 'i', 'o', 'u'}

    with open(filename) as file:
        return {word for word in file if vowels < set(word)}


results = get_vocalic('words.txt')

for result in results:
    print(result.strip())

print(f'Total words found: {len(results)}')
