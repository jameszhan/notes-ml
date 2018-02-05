# -*- coding: utf-8 -*-
# The following code just can be run in python3


class Iterable(object):
    def __init__(self):
        self.counter = 10

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= 0:
            raise StopIteration()
        print('get next, current is %d.' % self.counter)
        self.counter -= 1
        return self.counter


l = Iterable()
print([x for x in l])