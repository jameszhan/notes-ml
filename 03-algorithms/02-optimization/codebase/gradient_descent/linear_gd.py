# -*- coding: utf-8 -*-
import numpy as np

def linear_gd(X, Y, alpha=0.01, epsilon=1e-6):
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