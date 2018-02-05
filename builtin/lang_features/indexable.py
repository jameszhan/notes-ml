# -*- coding: utf-8 -*-


class Indexable(object):
    def __getitem__(self, i):
        if i > 10:
            raise StopIteration()
        print 'get object {0}, locals: {1}'.format(i, locals())
        return i


print [x for x in Indexable()]