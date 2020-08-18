# Problem: given two dictionary arguments, return a dictionary where the key-values don't match
# Input: two dict objects
# Output: dict object where the keys are discrepancy locations and values are a list of the mismatch from each side

def get_dict_diff(left_side: dict, right_side: dict) -> dict:
    """ Calculate differences between two different dict objects """

    if not isinstance(left_side, dict) or not isinstance(right_side, dict):
        return {'Error': 'Dicts only please'}   # raise error here?  print message?  hmm... options...

    diff_result = {}

    all_keys = left_side.keys() | right_side.keys()

    for key in all_keys:
        if left_side.get(key) != right_side.get(key):
            diff_result[key] = [left_side.get(key), right_side.get(key)]

    return diff_result


print(get_dict_diff({'a': 1, 'b': 2}, {'a': 1, 'b': 2}))
print(get_dict_diff({'a': 1, 'b': 2}, {'a': 1, 'b': 3}))
print(get_dict_diff({'a': 1, 'b': 2}, {'a': 3, 'b': 2}))
print(get_dict_diff({'a': 1, 'b': 2}, {'a': 1, 'c': 2}))
