# Problem: define a class that take two arguments on init, a sequence and a number.  Iterable until it reaches the
#          number, repeating items from the sequence as needed
# Input: sequence and int x
# Output: sequence of length x, repeating as needed

class Circle:
    def __init__(self, sequence, length):
        self.data = sequence
        self.max_iterations = length

    def __iter__(self):
        return CircleIterable(self.data, self.max_iterations)


class CircleIterable:
    def __init__(self, sequence, length):
        self.data = sequence
        self.max_iterations = length
        self.data_length = len(self.data)
        self.index = 0

    def __next__(self):
        if self.index < self.max_iterations:
            value = self.data[self.index % self.data_length]
            self.index += 1
            return value
        else:
            raise StopIteration


if __name__ == '__main__':
    test = Circle('abc', 20)
    final_length = 0

    for letter in test:
        final_length += 1
        print(letter, end='')

    print()
    print(f'Final length: {final_length}')
