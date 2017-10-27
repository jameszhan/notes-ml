# -*- coding: utf-8 -*-
import numpy as np


def bgd(X, Y, alpha=0.01, epsilon=1e-8, trace=True):
    m = len(X)
    _X = np.column_stack((np.ones(m), X))
    m, n = np.shape(_X)
    theta, sse2, cnt = np.ones(n), 0, 0
    Xt = _X.T
    while True:
        loss = np.dot(_X, theta) - Y
        # sse = np.sum(loss ** 2) / (2 * m)
        # sse = loss.T.dot(loss) / (2 * m)
        sse = np.dot(loss.T, loss) / (2 * m)
        if abs(sse - sse2) < epsilon:
            break
        else:
            sse2 = sse

        if trace:
            print "[ Epoch {0} ] theta = {1}, loss = {2}, error = {3})".format(cnt, theta, loss, sse)

        gradient = np.dot(Xt, loss) / m
        theta -= alpha * gradient
        cnt += 1
    return theta


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    X = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Y = [1.99, 3.89, 5.80, 7.83, 9.80, 11.77, 13.80, 15.75, 17.71]

    b, a = bgd(X, Y, 0.05, 1e-6)

    print 'y = {0} * x + {1}'.format(a, b)

    x = np.array(X)
    plt.plot(x, Y, 'o', label='Original data', markersize=5)
    plt.plot(x, a * x + b, 'r', label='Fitted line')
    plt.show()

    x = [(0., 3), (1., 3), (2., 3), (3., 2), (4., 4)]
    y = [95.364, 97.217205, 75.195834, 60.105519, 49.342380]

    _theta = bgd(x, y, 0.1, 1e-8)
    print 'theta = {0}'.format(_theta)


