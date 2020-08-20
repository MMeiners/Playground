# Problem: open a file and return the final line inside
# Input: filename string
# Output: final string text

def get_final_line(filename: str) -> str:
    """ Get the final line in the given file """

    try:
        final_line = ''

        with open(filename) as file:
            for line in file:
                final_line = line

        return final_line
    except (TypeError, ValueError):
        return 'Error!'


print(get_final_line('test_file.txt'), end='')
