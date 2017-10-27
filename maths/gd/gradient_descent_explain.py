# -*- coding: utf-8 -*-
import numpy as np


def hypothesis(x, theta):
    return np.dot(x, theta)


def loss(x, y, theta):
    return hypothesis(x, theta) - y


def grad(x_t, diffs, m):
    return np.dot(x_t, diffs) / m


def J(theta, x, y, m):
    diffs = loss(x, y, theta)
    return np.dot(diffs.T, diffs) / m


def bgd(x, y, alpha=0.01, epsilon=1e-8):
    m, sse2 = len(x), 0
    x_0 = np.ones(m)
    xx = np.column_stack((x_0, x))
    m, n = np.shape(xx)
    x_t, theta = xx.T, np.ones(n)
    while True:
        diffs = loss(xx, y, theta)

        sse = J(theta, xx, y, m)
        if abs(sse - sse2) < epsilon:
            break
        else:
            sse2 = sse

        gradient = grad(x_t, diffs, m)
        theta -= alpha * gradient
    return theta


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]
    price = [2.000, 2.500, 2.900, 3.147, 4.515, 4.903, 5.365, 5.704, 6.853, 7.971, 8.561, 10.000, 11.280, 12.900]

    b, a = bgd(np.subtract(year, 2000), price, 0.01, 1e-8)

    x_axis = np.linspace(1999, 2015, 10000)

    for i in range(len(year)):
        plt.scatter(year[i], price[i])

    def linear_equation(x, a, b):
        return b + a * (x - 2000)

    print 'y = {0} * (x - 2000) + {1}'.format(a, b)
    plt.plot(x_axis, [linear_equation(x, a, b) for x in x_axis], 'r:')
    plt.grid(True)
    plt.show()

