# -*- coding: utf-8 -*-


def derivative(g, dx=1e-6):
    return lambda x: (g(x + dx) - g(x)) / dx


def cube(x):
    return x ** 3


print('((derivative cube) 5) = {0}'.format(derivative(cube)(5)))