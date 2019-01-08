# -*- coding: utf-8 -*-
import random


def pi(n):
    k = 0
    for i in range(n):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            k = k + 1
    return 4 * k * 1.0 / n


for i in range(1, 8):
    v = 10 ** i
    print('pi({0}) = {1}'.format(v, pi(v)))