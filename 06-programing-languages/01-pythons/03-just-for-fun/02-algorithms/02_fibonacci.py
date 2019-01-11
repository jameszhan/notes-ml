# -*- coding: utf-8 -*-
import math


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci2(n):
    if n < 2:
        return n
    else:
        x, y = 1, 0
        for i in range(2, n + 1):
            x, y = y, x
            x = x + y
        return x


def fibonacci3(n):
    sqrt5 = math.sqrt(5)
    c1, c2 = (1 + sqrt5) / 2, (1 - sqrt5) / 2
    return math.floor((math.pow(c1, n) - math.pow(c2, n))/sqrt5)


if __name__ == '__main__':
    import time

    r = range(0, 35, 5)

    start = time.time()
    fibs = [fibonacci(i) for i in r]
    print('Time: {0}, fibonacci({1}) = {2}'.format(
        time.time() - start, r, fibs))

    start = time.time()
    fibs = [fibonacci2(i) for i in r]
    print('Time: {0}, fibonacci2({1}) = {2}'.format(
        time.time() - start, r, fibs))

    start = time.time()
    fibs = [fibonacci3(i) for i in r]
    print('Time: {0}, fibonacci3({1}) = {2}'.format(
        time.time() - start, r, fibs))

    r = range(0, 1000, 100)

    start = time.time()
    fibs = [fibonacci2(i) for i in r]
    print('Time: {0}, fibonacci2({1}) = {2}'.format(
        time.time() - start, r, fibs))

    start = time.time()
    fibs = [fibonacci3(i) for i in r]
    print('Time: {0}, fibonacci3({1}) = {2}'.format(
        time.time() - start, r, fibs))
