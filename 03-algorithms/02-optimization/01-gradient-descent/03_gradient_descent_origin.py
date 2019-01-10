# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def gd(X, Y, alpha=0.01, epsilon=1e-6):
    m, n = len(X), len(X[0])
    theta = [1 for i in range(n)]
    sse2, cnt = 0, 0
    while True:
        gradient = [0 for i in range(n)]
        for j in range(n):
            for i in range(m):
                hypothesis = sum(X[i][jj] * theta[jj] for jj in range(n))
                loss = hypothesis - Y[i]
                gradient[j] += X[i][j] * loss
            gradient[j] = gradient[j] / m
        for j in range(n):
            theta[j] = theta[j] - alpha * gradient[j]

        sse = 0
        for i in range(m):
            loss = sum(X[i][jj] * theta[jj] for jj in range(n)) - Y[i]
            sse += loss ** 2
        sse = sse / (2 * m)

        print("[ Epoch {0} ] theta = {1}, gd = {2}, sse = {3})".format(cnt, theta, gradient, sse))
        cnt += 1
        if abs(sse2 - sse) < epsilon:
            break
        else:
            sse2 = sse
    return theta


X = [(1, 1.), (1, 2.), (1, 3.), (1, 4.), (1, 5.), (1, 6.), (1, 7.), (1, 8.), (1, 9.)]
Y = [0.199, 0.389, 0.580, 0.783, 0.980, 1.177, 1.380, 1.575, 1.771]

b, a = gd(X, Y, 0.05, 1e-6)

print('y = {0} * x + {1}'.format(a, b))

x = np.array(X)
plt.plot(x, Y, 'o', label='Original data', markersize=5)
plt.plot(x, a * x + b, 'r', label='Fitted line')
plt.show()
