# Problem: for a given word, find words with a matching gematria score
# Input: word string
# Output: list of words

from ex35a_gematria_pt1 import get_gematria
from typing import List

gematria_values = get_gematria()


def get_gematria_score(word: str) -> int:
    """ Score the given word """

    return sum([gematria_values.get(letter, 0) for letter in word])


def find_gematria_matches(word: str) -> List[str]:
    """ Given a word, find words with the same gematria score """

    score = get_gematria_score(word)

    with open('words.txt') as file:
        return [match.strip() for match in file if get_gematria_score(match) == score]


test_word = 'apple'
gematria_matches = find_gematria_matches(test_word)
print(gematria_matches)
print(f'Score for {test_word} is {get_gematria_score(test_word)}, {len(gematria_matches)} matches found')
