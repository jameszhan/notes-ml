# -*- coding: utf-8 -*-
import numpy as np

a = [[6, 5], [4, 3], [2, 1]]
print("sort({0}) => {1}".format(a, np.sort(a)))
print("argsort({0}) => {1}".format(a, np.argsort(a)))

b = [6, 5, 4, 3, 2, 1]
print("sort({0}) => {1}".format(b, np.sort(b)))
print("argsort({0}) => {1}".format(b, np.argsort(b)))

print("r_[b, b] => {0}".format(np.r_[b, b]))

print("c_[b, b] => {0}".format(np.c_[b, b]))