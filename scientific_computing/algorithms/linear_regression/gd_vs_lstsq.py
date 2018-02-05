# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def gd(X, Y, alpha = 0.01, epsilon=1e-32):
    m = len(X)
    a, b = 0, 0
    sse0 = 0
    while True:
        grad_a, grad_b = 0, 0
        for i in range(m):
            diff = a * X[i] + b - Y[i]
            grad_a += X[i] * diff
            grad_b += diff

        grad_a = grad_a / m
        grad_b = grad_b / m

        a -= alpha * grad_a
        b -= alpha * grad_b

        sse1 = 0
        for j in range(m):
            sse1 += (a * X[j] + b - Y[j]) ** 2 / (2 * m)

        if abs(sse0 - sse1) < epsilon:
            break
        else:
            sse0 = sse1
    return a, b


X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
Y = np.array([0.199, 0.389, 0.580, 0.783, 0.980, 1.177, 1.380, 1.575, 1.771])

a1, b1 = gd(X, Y, 0.05, 1e-6)
a2, b2 = gd(X, Y, 0.05, 1e-8)
a3, b3 = gd(X, Y, 0.05, 1e-32)


print('y = {0} * x + {1}'.format(a1, b1))
print('y = {0} * x + {1}'.format(a2, b2))
print('y = {0} * x + {1}'.format(a3, b3))

A = np.vstack([X, np.ones(len(X))]).T
a, b = np.linalg.lstsq(A, Y)[0]

print('y = {0} * x + {1}'.format(a, b))


x = np.array(X)
plt.plot(x, Y, 'o', label='Original data', markersize=5)
plt.plot(x, a1 * x + b1, 'r--', label='Fitted line')
plt.plot(x, a2 * x + b2, 'g--', label='Fitted line')
plt.plot(x, a3 * x + b3, 'b--', label='Fitted line')
plt.plot(x, a * x + b, 'm--', label='Fitted line')
plt.show()