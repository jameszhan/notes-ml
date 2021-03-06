# -*- coding: utf-8 -*-

import numpy as np


def H(*P):
    p = 0.0
    for px in P:
        p += px * np.log2(px)
    return -p


print(H(0.5, 0.5))
print(H(0.3, 0.7))
print(H(0.01, 0.99))
print(H(0.00001, 0.99999))


print("====================")

print(H(0.25, 0.25, 0.25, 0.25))
print(H(0.7, 0.1, 0.1, 0.1))
print(H(0.9, 0.09, 0.009, 0.001))
print(H(0.999, 0.0009, 0.00009, 0.00001))
print(H(0.99999, 0.000009, 0.0000009, 0.0000001))


print("====================")

print(H(0.2, 0.2, 0.2, 0.2, 0.2))
print(H(0.1, 0.1, 0.1, 0.1, 0.6))
print(H(0.01, 0.01, 0.01, 0.01, 0.96))
print(H(0.5, 0.3, 0.1, 0.08, 0.02))
print(H(0.3, 0.3, 0.3, 0.05, 0.05))