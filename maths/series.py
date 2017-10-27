# -*- coding: utf-8 -*-

import numpy as np


def factorial(n):
    i, f = 0, 1.0
    while i < n:
        f *= (i + 1)
        i += 1
    return f


# Count e
e = np.sum([1.0 / factorial(i) for i in range(1000)])
print e

# Count π
pi = 4 * np.sum([(1.0 * np.power(-1, i))/ (2 * i + 1) for i in range(100000)])
print pi
