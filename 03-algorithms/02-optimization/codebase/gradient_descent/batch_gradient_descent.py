# -*- coding: utf-8 -*-
import numpy as np


def bgd(x, y, h, cost, hypothesis, alpha=0.01, epsilon=1e-6):
    m, n = np.shape(x)
    _x = np.column_stack((np.ones(m), x))
    theta, j2, cnt = np.ones(n), 0, 0
    xt = np.transpose(_x)
    while True:
        loss = hypothesis(_x, y)
        gradient = np.dot(xt, loss) / m
        theta -= alpha * gradient


def bgd2(rows, labels, hypothesis, cost, alpha=0.01, epsilon=1e-6, trace=True):
    m = len(rows)
    _X = np.column_stack((np.ones(m), rows))
    m, n = np.shape(_X)
    theta, j1, cnt = np.ones(n), 0, 0
    xt = _X.T
    while True:
        loss = hypothesis(_X, theta) - labels
        gradient = np.dot(xt, loss) / m
        theta -= alpha * gradient

        j = 0
        for k in range(m):
            j += cost(_X[k], theta, labels[k])
        j = j / m
        if trace:
            print("[ Epoch {0} ] theta = {1}, loss = {2}, error = {3})".format(cnt, theta, loss, j))

        if abs(j - j1) < epsilon:
            break
        else:
            j1 = j

        cnt += 1
    return theta


def gd(X, Y, alpha=0.01, epsilon=1e-6):
    m, n = np.shape(X)
    theta = np.ones(n)
    sse2, cnt = 0, 0
    Xt = np.transpose(X)
    while True:
        hypothesis = np.dot(X, theta)
        loss = hypothesis - Y
        gradient = np.dot(Xt, loss) / m
        theta -= alpha * gradient

        loss2 = np.dot(X, theta) - Y
        sse = np.dot(loss2.T, loss2) / (2 * m)
        print("[ Epoch {0} ] theta = {1}, gradient = {2}, sse = {3})".format(cnt, theta, gradient, sse))
        cnt += 1
        if abs(sse2 - sse) < epsilon:
            break
        else:
            sse2 = sse
    return theta


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


def hypothesis(X, theta):
    return 1.0 / (1 + np.exp(-np.dot(X, theta)))

def cost(hypothesis, x, theta, y):
    h = hypothesis(x, theta)

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


if __name__ == '__main__':
    print(hypothesis([(1, 2), (3, 4), (5, 6)], [2, 2]))