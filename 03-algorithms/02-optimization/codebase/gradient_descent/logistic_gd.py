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


def logistic_gd(X, Y, alpha=0.01, epsilon=1e-6, trace=True):
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
            print("[ Epoch {0} ] theta = {1}, loss = {2}, error = {3})".format(
                cnt, theta, loss, j))

        if abs(j - j1) < epsilon:
            break
        else:
            j1 = j

        cnt += 1
    return theta
