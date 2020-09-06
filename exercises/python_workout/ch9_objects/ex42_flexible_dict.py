# Problem: inherit from dict to create a new class that will try to convert a missing key and search again.
#          For example, if the key is int 1, also look for str(1) if int 1 isn't found
# Input: a series of keys
# Output: value object found in the dict

class FlexibleDict(dict):
    pass


if __name__ == '__main__':
    test_dict = FlexibleDict()
    test_dict[1] = 'one int'
    test_dict['2'] = 'two str'
    test_dict[3] = 'three int'
    test_dict['3'] = 'three str'

    print(f'Search int 1, found {test_dict[1]}')
    print(f'Search str 1, found {test_dict["1"]}')
    print(f'Search int 2, found {test_dict[2]}')
    print(f'Search int 3, found {test_dict[3]}')
