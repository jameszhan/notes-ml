# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def gd(X, Y, alpha=0.01, epsilon=1e-6):
    m, n = np.shape(X)
    theta = np.ones(n)
    sse2, cnt = 0, 0
    Xt = np.transpose(X)
    while True:
        hypothesis = np.dot(X, theta)
        loss = hypothesis - Y
        # sse = sum(l ** 2.0 for l in loss) / (2 * m)
        sse = np.dot(loss.T, loss) / (2 * m)

        print("[ Epoch {0} ] theta = {1}, loss = {2}, error = {3})".format(cnt, theta, loss, sse))
        cnt += 1
        if abs(sse2 - sse) < epsilon:
            break
        else:
            sse2 = sse

        gradient = np.dot(Xt, loss) / m
        theta -= alpha * gradient
    return theta


X = [(1, 1.), (1, 2.), (1, 3.), (1, 4.), (1, 5.), (1, 6.), (1, 7.), (1, 8.), (1, 9.)]
Y = [0.199, 0.389, 0.580, 0.783, 0.980, 1.177, 1.380, 1.575, 1.771]

b, a = gd(X, Y, 0.05, 1e-6)

print('y = {0} * x + {1}'.format(a, b))

x = np.array(X)
plt.plot(x, Y, 'o', label='Original data', markersize=5)
plt.plot(x, a * x + b, 'r', label='Fitted line')
plt.show()