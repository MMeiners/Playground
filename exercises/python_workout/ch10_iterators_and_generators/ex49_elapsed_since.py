# Problem: write a generator function that takes an iterable and returns a tuple where the first element is
#          the time since last iteration and second element is the next item from the iterable
# Input: iterable
# Output: tuple(time between yields, next item)

from time import perf_counter, sleep
from random import randint


def elapsed_since(items) -> tuple:
    """ Return elapsed time and an item per iteration """

    last_iteration_time = 0.0

    for item in items:
        # in the book, instead of an if statement for the first case, the author set the initial time to None
        # and let an 'or' operator determine which value to use... not sure I like that... feels weird to rely on
        # short circuit evaluation, maybe due to all the SQL I write where the optimizer does as it pleases instead.
        # e.g. delta = current_time - (last_time or current_time)
        if last_iteration_time == 0.0:
            elapsed_time = 0.0
        else:
            elapsed_time = perf_counter() - last_iteration_time

        last_iteration_time = perf_counter()

        yield elapsed_time, item


if __name__ == '__main__':
    test_data = '0123456789'

    for each_tuple in elapsed_since(test_data):
        print(each_tuple)
        sleep(randint(1, 5))
