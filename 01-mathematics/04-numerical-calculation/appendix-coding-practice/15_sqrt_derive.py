# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def target(x, v):
    return x ** 2 - v


n = 5
X = np.linspace(-5, 5, 100)
plt.plot(X, target(X, n), 'r:')
plt.grid(True)
plt.show()


def binary_method(n, epsilon):
    l, r, i = 0, n, 0
    while True:
        m = (l + r) / 2.0
        print('[ Epoch {0} ] l = {1}, r = {2}, m = {3}'.format(i, l, r, m))
        guess = m ** 2
        if abs(n - guess) <= epsilon:
            break
        elif guess > n:
            r = m
        else:
            l = m
        i += 1
    return m


# newton method, n is positive integer
#
# Theory:
#
# slope of the tangent line is f'(Xn)
# [Xn, f(Xn)] is one point of the tangent line
# f(Xn) - 0 = f'(Xn) * (Xn - Xn+1)
# Xn+1 = Xn - f(Xn) / f'(Xn)
# f(x) = x ** 2 - n
# f'(x) = 2 * x
# Xn+1 = Xn - (Xn - n / Xn) / 2
# Xn+1 = (Xn + n / Xn) / 2
def newton_method(n, epsilon):
    guess, i = n, 0
    while abs(guess ** 2 - n) > epsilon:
        print('[ Epoch {0} ] guess = {1}, n = {2}'.format(i, guess, n))
        # f(x) = x ** 2 - n => x0 - f(x0) / f'(x0) = (x0 + n / x0) / 2
        guess = (guess + n / guess) / 2.0
        i += 1
    return guess


print('[Binary] sqrt({0}) = {1}.\n'.format(n, binary_method(n, 1e-6)))
print('[Newton] sqrt({0}) = {1}.\n'.format(n, newton_method(n, 1e-6)))

