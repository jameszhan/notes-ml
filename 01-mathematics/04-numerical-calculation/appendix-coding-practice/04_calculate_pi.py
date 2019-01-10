# -*- coding: utf-8 -*-
import random
import numpy as np


def pi_by_dice(n):
    k = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            k = k + 1
    return 4 * k * 1.0 / n


for i in range(1, 8):
    v = 10 ** i
    print('pi({0}) = {1}'.format(v, pi_by_dice(v)))
    

n = 100000
pi_by_series = np.sum(4.0 / np.r_[1:n:4, -3:-n:-4])

print("pi_by_series =", pi_by_series)
