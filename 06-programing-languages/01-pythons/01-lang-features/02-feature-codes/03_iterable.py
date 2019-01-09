# -*- coding: utf-8 -*-

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


it = Iterable()
print([x for x in it])