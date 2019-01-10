# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# 牛顿法几何意义

X = np.linspace(-5, 20, 1000)
colors = ['r-.', 'g-.', 'b-.', 'y-.', 'c-.', 'm-.', 'k-.', 'w-.', 'r-.', 'g-.', 'b-.', 'y-.', 'c-.', 'm-.', 'k-.', 'w-.']


def tangent(slope, x1, x):
    return slope * (x - x1)


def derivative(g, epsilon=1e-8):
    dx = epsilon
    return lambda x: (g(x + dx) - g(x)) / dx


def solve(g, initial, epsilon=1e-8):
    guess, i = initial, 0
    while abs(g(guess)) > epsilon:
        print('[ Epoch {0} ] guess = {1}'.format(i, guess))
        slope = derivative(g, epsilon)(guess)
        guess -= (g(guess) / slope)
        plt.plot(X, tangent(slope, guess, X), colors[i])
        plt.scatter(guess, 0)
        i += 1
    return guess


def square(x):
    return x ** 2 - 5


plt.plot(X, square(X), 'k-')
print(solve(square, 10, 1e-8))

plt.grid(True)
plt.show()
