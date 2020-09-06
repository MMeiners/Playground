# Problem: inherit from dict to create a new class that will try to convert a missing key and search again.
#          For example, if the key is int 1, also look for str(1) if int 1 isn't found
# Input: a series of keys
# Output: value object found in the dict

class FlexibleDict(dict):
    """ A more flexible dict index """

    def __getitem__(self, item):
        """ override normal [] access to a dict trying to cast the key to match """

        key = item

        try:
            if key in self:
                pass
            elif int(key) in self:
                key = int(key)
            elif str(key) in self:
                key = str(key)
            else:
                raise ValueError

            return super().__getitem__(key)
        except (ValueError, TypeError):
            return 'nothing here!'


if __name__ == '__main__':
    test_dict = FlexibleDict()
    test_dict[1] = 'int one'
    test_dict['1'] = 'str one'
    test_dict['2'] = 'str two'
    test_dict[3] = 'int three'

    print(f'Search int 1, found {test_dict[1]}')
    print(f'Search str 1, found {test_dict["1"]}')
    print(f'Search int 2, found {test_dict[2]}')
    print(f'Search str 3, found {test_dict["3"]}')
    print(f'Search str a, found {test_dict["a"]}')
    print(f'Search int 20, found {test_dict[20]}')
