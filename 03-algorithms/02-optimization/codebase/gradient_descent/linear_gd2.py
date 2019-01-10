# -*- coding: utf-8 -*-
import numpy as np

def linear_gd(X, Y, alpha=0.01, epsilon=1e-8, trace=True):
    m = len(X)
    _X = np.column_stack((np.ones(m), X))
    m, n = np.shape(_X)
    theta, sse2, cnt = np.ones(n), 0, 0
    Xt = _X.T
    while True:
        loss = np.dot(_X, theta) - Y
        sse = np.dot(loss.T, loss) / (2 * m)
        if abs(sse - sse2) < epsilon:
            break
        else:
            sse2 = sse

        if trace:
            print("[ Epoch {0} ] theta = {1}, loss = {2}, error = {3})".format(cnt, theta, loss, sse))

        gradient = np.dot(Xt, loss) / m
        theta -= alpha * gradient
        cnt += 1
        
    return theta