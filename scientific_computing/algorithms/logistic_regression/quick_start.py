# -*- coding: utf-8 -*-
import numpy as np


def h(x, theta):
    return 1 / (1 + np.exp(-np.dot(x, theta)))


def cost(x, y, theta):
    _h = h(x, theta)
    if y == 1:
        return -np.log(_h)
    else:
        return -np.log(1 - _h)


def J(X, Y, theta):
    m, n = np.shape(X)
    loss = 0
    for k in range(m):
        loss += cost(X[k], Y[k], theta)
    return loss / m


def bgd(X, Y, alpha=0.01, epsilon=1e-6, trace=True):
    m = len(X)
    _X = np.column_stack((np.ones(m), X))
    m, n = np.shape(_X)
    theta, j1, cnt = np.ones(n), 0, 0
    Xt = _X.T

    while True:
        loss = h(_X, theta) - Y
        gradient = np.dot(Xt, loss) / m
        theta -= alpha * gradient

        j = J(_X, Y, theta)

        if trace:
            print("[ Epoch {0} ] theta = {1}, loss = {2}, error = {3})".format(cnt, theta, loss, j))

        if abs(j - j1) < epsilon:
            break
        else:
            j1 = j

        cnt += 1
    return theta


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

    theta2 = bgd(X, Y, 0.5)
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







