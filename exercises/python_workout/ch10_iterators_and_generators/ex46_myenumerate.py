# Problem: reimplement enumerate()
# Input: iterable object
# Output: a tuple (index, element) for each iteration

class MyEnumerate:
    def __init__(self, some_iterable):
        self.data = some_iterable
        self.data_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.data_index < len(self.data):
            to_return = (self.data_index, self.data[self.data_index])
            self.data_index += 1
            return to_return
        else:
            raise StopIteration


if __name__ == '__main__':
    for index, value in MyEnumerate('abc'):
        print(f'{index}: {value}')
