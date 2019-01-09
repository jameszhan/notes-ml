# -*- coding: utf-8 -*-
import random


def shuffle(l):
    n = len(l)
    for i in range(n):
        j = random.randint(0, n - 1)
        l[i], l[j] = l[j], l[i]
    return l


items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print 'Before Shuffle:\t{0}'.format(items)
print 'After Shuffle:\t{0}'.format(shuffle(items))
