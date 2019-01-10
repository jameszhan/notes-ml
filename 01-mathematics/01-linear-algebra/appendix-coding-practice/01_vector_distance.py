# -*- coding: utf-8 -*-
import numpy as np

v1 = np.mat([1, 2, 3])
v2 = np.mat([5, 7, 9])

print('v1 = {0}, v2 = {1}'.format(v1, v2))


def manhattan(x1, x2):
    return np.sum(np.abs(x1 - x2))


def euclidean(x1, x2):
    v = x1 - x2
    return np.sqrt(np.dot(v, v.T))


def chebyshev(x1, x2):
    return np.max(np.abs(x1 - x2))


print('manhattan = {0}\neuclidean = {1}\nchebyshev = {2}'.format(manhattan(v1, v2), euclidean(v1, v2).item(0), chebyshev(v1, v2)))

