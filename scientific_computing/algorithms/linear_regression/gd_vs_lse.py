# -*- coding: utf-8 -*-
import numpy as np
from gradient_descent import bgd


# define least square estimation function: Y = aX + b
def lse(X, Y):
    cov_mat = np.cov(X, Y, ddof=0)
    a = cov_mat[0][1] / cov_mat[0][0]
    Y_mean = Y.mean()
    X_mean = X.mean()
    b = Y_mean - a * X_mean

    Y_pred = a * X + b
    Rsquare = np.mean((Y_pred - Y_mean) ** 2) / np.var(Y)

    return a, b, Rsquare


# define gradient descent function: Y = aX + b
def gd(X, Y, alpha=0.01, epsilon=1e-32):
    m = len(X)
    a, b, sse2 = 0, 0, 0
    while True:
        loss = a * X + b - Y
        lossT = loss.T
        sse = np.dot(lossT, loss) / (2 * m)
        if abs(sse2 - sse) < epsilon:
            break
        else:
            sse2 = sse

        grad_a = np.dot(lossT, X) / m
        grad_b = np.dot(lossT, np.ones(m)) / m
        a -= alpha * grad_a
        b -= alpha * grad_b
    return a, b


X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
Y = np.array([0.199, 0.389, 0.580, 0.783, 0.980, 1.177, 1.380, 1.575, 1.771])

print(lse(X, Y))
print(gd(X, Y, 0.05))
print(bgd(X, Y, 0.05, 1e-32, False))