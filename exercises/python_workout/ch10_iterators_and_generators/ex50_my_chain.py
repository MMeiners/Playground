# Problem: implement a version of itertools.chain, taking any number of iterables and using a generator function
#          to return them one by one in order.
# Input: some iterables
# Output: elements of the iterables one by one

def my_chain(*bunch_of_iterables):
    """ Given some iterables, return one by one in a generator function """

    for an_iterable in bunch_of_iterables:
        for an_element in an_iterable:
            yield an_element


if __name__ == '__main__':
    for each_one in my_chain([1, 2, 3], 'abc', (4, 5)):
        print(each_one)
