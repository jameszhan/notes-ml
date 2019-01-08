# -*- coding: utf-8 -*-

import operator

m1 = [
    [4, 3, 2, 1],
    [3, 2, 1, 4],
    [2, 1, 4, 3],
    [1, 4, 3, 2]
]

m2 = m1.copy()

print(m1)
m1.sort(key=operator.itemgetter(0))
m2.sort(key=lambda m: m[0])
print(m2)
print(m1)

