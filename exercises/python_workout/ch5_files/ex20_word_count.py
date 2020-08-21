# Problem: mimic the unix utility wc which returns word/character stats for the file
# Input: filename string
# Output: number of characters, number of words, number of lines, number of unique words each on a different line

def get_word_counts(filename: str) -> str:
    """ Calculate basic word statistics for a file """

    file_stats = {'characters': 0,
                  'words': 0,
                  'lines': 0,
                  'unique_words': set()}

    try:
        with open(filename) as file:
            for line in file:
                file_stats['characters'] += len(line)
                file_stats['words'] += len(line.strip().split())
                file_stats['lines'] += 1
                file_stats['unique_words'].update(line.strip().split())

        return f"Characters: {file_stats['characters']}\n" \
               f"Words: {file_stats['words']}\n" \
               f"Lines: {file_stats['lines']}\n" \
               f"Unique Words: {len(file_stats['unique_words'])}"
    except (ValueError, TypeError):
        return 'Error'


print(get_word_counts('wcfile.txt'))
