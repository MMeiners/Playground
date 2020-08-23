# Problem: write a function that reads json test files from a directory and reports a summary of test scores
# Input: directory string holding test score json files
# Output: summary of score data

import pathlib
import json


def print_scores(directory: str) -> str:
    """ Summarize json test score data found in the given directory """

    collected_scores = {}
    score_summary = ''
    directory_path = pathlib.Path(directory)

    for file_path in directory_path.glob('*.json'):
        filename = str(file_path)
        collected_scores[filename] = {}

        with open(file_path) as file:
            for record in json.load(file):
                for subject, score in record.items():
                    collected_scores[filename].setdefault(subject, [])
                    collected_scores[filename][subject].append(score)

    for filename, record in collected_scores.items():
        score_summary += filename + '\n'

        for subject, scores in record.items():
            score_summary += f'\t{subject}: min {min(scores)}, max {max(scores)}, average {sum(scores)/len(scores)}\n'

    return score_summary


print(print_scores('scores'))
