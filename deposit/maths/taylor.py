# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def factorial(n):
    c, f = 0, 1.0
    while c < n:
        f *= (c + 1)
        c += 1
    return f


def item(x, n):
    return np.power(x, n) / factorial(n)


def taylor(x, n):
    return np.sum([item(x, k) for k in range(0, n)])


X = np.linspace(0, 5, 1000)
plt.grid(True)

plt.plot(X, [taylor(i, 2) for i in X], 'r:')    # 红色
plt.plot(X, [taylor(i, 3) for i in X], 'g:')    # 绿色
plt.plot(X, [taylor(i, 5) for i in X], 'b-.')   # 蓝色
plt.plot(X, [taylor(i, 7) for i in X], 'm--')   # 紫红色
plt.plot(X, [taylor(i, 9) for i in X], 'y-.')   # 黄色
plt.plot(X, np.exp(X), 'k:')                    # 黑色

plt.show()



