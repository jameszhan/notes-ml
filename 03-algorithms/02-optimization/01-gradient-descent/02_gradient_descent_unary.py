# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def gd(X, Y, alpha=0.01, epsilon=1e-8):
    m = len(X)
    a, b, sse2 = 0, 0, 0
    while True:
        grad_a, grad_b = 0, 0
        for i in range(m):
            diff = a * X[i] + b - Y[i]
            grad_a += X[i] * diff
            grad_b += diff

        a -= alpha * grad_a / m
        b -= alpha * grad_b / m

        sse = 0
        for j in range(m):
            sse += (a * X[j] + b - Y[j]) ** 2 / (2 * m)

        if abs(sse2 - sse) < epsilon:
            break
        else:
            sse2 = sse
    return a, b


X = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Y = [0.199, 0.389, 0.580, 0.783, 0.980, 1.177, 1.380, 1.575, 1.771]

a, b = gd(X, Y, 0.05, 1e-6)

print('y = {0} * x + {1}'.format(a, b))

x = np.array(X)
plt.plot(x, Y, 'o', label='Original data', markersize=5)
plt.plot(x, a * x + b, 'r', label='Fitted line')
plt.show()