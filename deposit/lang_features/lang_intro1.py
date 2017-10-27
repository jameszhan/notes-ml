#!/usr/bin/env python


class sample(object):
    def __init__(self):
        print 'construct'

    def do_something(self, x):
        print 'invoking with ', x


def func(x, y):
    if y == 0:
        return "error"
    return x + y
