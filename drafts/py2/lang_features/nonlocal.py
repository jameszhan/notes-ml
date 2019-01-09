# -*- coding: utf-8 -*-
# python 2.x 不支持 nonlocal


def counter(init):
    nonlocal = {'v': init}

    def inc():
        nonlocal['v'] += 1
        print 'inc.locals: {0}'.format(locals())
        return nonlocal['v']

    print 'counter.locals: {0}'.format(locals())
    return inc


c = counter(0)
c2 = counter(10)

for _ in range(10):
    print 'c = {0}, c2 = {1}'.format(c(), c2())


def counter2(init):

    def inc():
        inc.v += 1
        print 'inc.locals: {0}'.format(locals())
        return inc.v

    inc.v = init

    print 'counter2.locals: {0}'.format(locals())
    return inc


c = counter2(0)
c2 = counter2(10)

for _ in range(10):
    print 'c = {0}, c2 = {1}'.format(c(), c2())


def counter3(init):

    class nonlocal:
        v = init

    def inc():
        nonlocal.v += 1
        print 'inc.locals: {0}'.format(locals())
        return nonlocal.v

    print 'counter3.locals: {0}'.format(locals())
    return inc


c = counter3(0)
c2 = counter3(10)

for _ in range(10):
    print 'c = {0}, c2 = {1}'.format(c(), c2())


class Nonlocals(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def counter4(init):
    nonlocals = Nonlocals(v=init)

    def inc():
        nonlocals.v += 1
        print 'inc.locals: {0}'.format(locals())
        return nonlocals.v
    print 'counter4.locals: {0}'.format(locals())
    return inc


c = counter4(0)
c2 = counter4(10)

for _ in range(10):
    print 'c = {0}, c2 = {1}'.format(c(), c2())

