# -*- coding: utf-8 -*-
import numpy as np
from batch_gradient_descent import bgd


def h(x, theta):
    return 1 / (1 + np.exp(-np.dot(x, theta)))


def cost(x, theta, y):
    _h = h(x, theta)
    if y == 1:
        return -np.log(_h)
    else:
        return -np.log(1 - _h)


def predict2d(theta, x, y):
    data = [1, x, y]
    v = h(theta, data)
    print('predict ({0}, {1}) = {2}, z = {3}'.format(x, y, v, np.dot(theta, data)))
    return v


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    m = 12
    x1 = np.linspace(0, 6, m + 1)
    x2 = np.linspace(0, 6, m + 1)
    X, Y = [], []

    print(x1)
    for i in range(m):
        for j in range(m):
            X.append((x1[i], x2[j]))
            if x1[i] > 5 or x2[j] > 5 or x1[i] + x2[j] > 5:
                Y.append(1)
            else:
                Y.append(0)

    for i in range(len(X)):
        c, m = 'r', 'o'
        if Y[i] == 0:
            c, m = 'b', 'x'
        plt.scatter(X[i][0], X[i][1], c=c, marker=m)

    plt.grid(True)
    plt.show()

    theta2 = bgd(X, Y, h, cost, 0.5)
    print('theta = {0}'.format(theta2))

    predict2d(theta2, 10, 10)
    predict2d(theta2, 10, 1)
    predict2d(theta2, 2, 8)
    predict2d(theta2, 5, 5)
    predict2d(theta2, 4, 4)
    predict2d(theta2, 3, 4)
    predict2d(theta2, 3, 3)
    predict2d(theta2, 2, 4)
    predict2d(theta2, 3, 2.5)
    predict2d(theta2, 2.5, 3)
    predict2d(theta2, 2.5, 2.5)
    predict2d(theta2, 3, 2)
    predict2d(theta2, 1, 1)
    predict2d(theta2, -3, -3)
    predict2d(theta2, -5, -5)
    predict2d(theta2, -10, -10)
