# -*- coding: utf-8 -*-

print 'locals = {0}'.format(locals())


def func(a, b=1, *c, **d):
    print 'locals = {0}'.format(locals())
    l = lambda args: locals()
    print l(c)


func(1, 2, 3, 4, 5, 6, 7, 8, d={'a': 1, 'b': 2})
