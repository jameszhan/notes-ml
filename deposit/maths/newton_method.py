# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def derivative(g, epsilon):
    dx = epsilon
    return lambda x: (g(x + dx) - g(x)) / dx


def solve(g, initial, epsilon):
    guess, i = initial, 0
    while abs(g(guess)) > epsilon:
        print '[ Epoch {0} ] guess = {1}'.format(i, guess)
        guess -= (g(guess) / (derivative(g, epsilon)(guess)))
        i += 1
    return guess


# 求解f(x) = x^2 - 5 = 0
print solve(lambda x: x ** 2 - 5, 5, 1e-8)

# 求解f(x) = x^2 - 2 = 0
print solve(lambda x: x ** 2 - 2, 2, 1e-8)


def sqrt(n):
    return solve(lambda x: x ** 2 - n, n, 1e-6)


def cube(n):
    return solve(lambda x: x ** 3 - n, n, 1e-6)


n = 5
print 'sqrt({0}) = {1}.\n'.format(n, sqrt(n), 10, 1e-6)
print 'cube({0}) = {1}.\n'.format(n, cube(n), 1e-6)


def solve_extremum(g, initial, epsilon):
    f = derivative(g, epsilon)
    x = solve(f, initial, epsilon)
    return x, g(x)


print '(x - 2) ** 2 = {0}, extremum = {1}.\n'.format(n, solve_extremum(lambda x: (x - 2) ** 2 - n, n, 1e-6))
print 'x ** 3 = {0}, extremum = {1}.\n'.format(n, solve_extremum(lambda x: x ** 3 - n, n, 1e-6))


X = np.linspace(-10, 10, 100)
plt.plot(X, (lambda x: (x - 2) ** 2 - n)(X), 'r:')
plt.plot(X, (lambda x: x ** 3 - n)(X), 'b:')
plt.grid(True)
plt.show()