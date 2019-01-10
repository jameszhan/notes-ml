# -*- coding: utf-8 -*-


def derivative(g, dx=1e-8):
    return lambda x: (g(x + dx) - g(x)) / dx


def cube(x):
    return x ** 3


def parabola(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


print('((derivative cube) 5) = {0}'.format(derivative(cube)(5)))

squarex = parabola(1, 0, 0)

print('((derivative squarex) 5) = {0}'.format(derivative(squarex)(5)))

squarex2 = parabola(2, -20, 5)

print('((derivative squarex2) 5) = {0}'.format(derivative(squarex2)(5)))
