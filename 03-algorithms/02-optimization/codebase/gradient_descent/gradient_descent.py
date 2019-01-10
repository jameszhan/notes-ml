# -*- coding: utf-8 -*-
import numpy as np

def bgd(X, Y, hypothesis, cost, alpha=0.01, epsilon=1e-6, trace=True):
    m = len(X)
    _X = np.column_stack((np.ones(m), X))
    m, n = np.shape(_X)
    theta, j1, cnt = np.ones(n), 0, 0
    xt = _X.T
    while True:
        loss = hypothesis(_X, theta) - Y
        gradient = np.dot(xt, loss) / m
        theta -= alpha * gradient

        j = 0
        for k in range(m):
            j += cost(_X[k], theta, Y[k])
        j = j / m
        if trace:
            print("[ Epoch {0} ] theta = {1}, loss = {2}, error = {3})".format(cnt, theta, loss, j))

        if abs(j - j1) < epsilon:
            break
        else:
            j1 = j

        cnt += 1
    return theta