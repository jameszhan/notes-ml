# -*- coding: utf-8 -*-


def derivative(g, epsilon=1e-8):
    dx = epsilon
    return lambda x: (g(x + dx) - g(x)) / dx


def gd(x_start, step, f, epsilon=1e-8):
    x = x_start
    for i in range(200):
        grad = derivative(f, epsilon)(x)
        x -= grad * step
        print('[ Epoch {0} ] grad = {1}, x = {2}'.format(i, grad, x))
        if abs(grad) < epsilon:
            break
    return x


def f(x):
    return (x - 3) ** 2 - 5


x = gd(100, 0.1, f)
print('extremum = ({0}, {1})'.format(x, f(x)))