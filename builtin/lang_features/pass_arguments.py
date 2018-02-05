# -*- coding: utf-8 -*-


def func(*x):
    print 'locals: {0}'.format(locals())
    if len(x) == 0:
        return None
    else:
        return x


print 'func() = {0}, func(1) = {1}, func(1, 2, 3) = {2}'.format(func(), func(1), func(1, 2, 3))


def func2(**x):
    print 'locals: {0}'.format(locals())
    if len(x) == 0:
        return None
    else:
        return x


print 'func2() = {0}, func2(1) = {1}, func2(1, 2, 3) = {2}'.format(func2(), func2(x=1), func2(a=1, b=2, c=3))