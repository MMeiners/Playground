# Problem: read from a passwd style file and write to a tab delimited file the username and user id
# Input: filename to read from, filename to write to
# Output: file written to disk

import csv


def passwd_to_csv(source_filename: str, output_filename: str) -> None:
    """ Extract usernames and user id from source and write to output """

    try:
        with open(source_filename) as source, open(output_filename, 'w', newline='') as output:
            csv_writer = csv.writer(output, delimiter='\t')

            for line in source:
                if line.startswith('#'):
                    continue
                else:
                    user_record = line.strip().split(':')
                    csv_writer.writerow([user_record[0], user_record[2]])
    except (TypeError, ValueError):
        raise   # what would be appropriate here?


passwd_to_csv('passwd.txt', 'passwd_extract.csv')   # maybe create a second function that reads it back?
