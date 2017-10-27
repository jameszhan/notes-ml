# -*- coding: utf-8 -*-


def solve(g, x0, x1, epsilon):
    gx0, gx1 = g(x0), g(x1)
    if gx0 > gx1:
        x0, x1 = x1, x0
    i = 0
    while True:
        x = (x0 + x1) / 2.0
        gx = g(x)
        print '[ Epoch {0} ] guess = {1}'.format(i, x)
        if abs(gx) < epsilon:
            return x
        else:
            if gx > 0:
                x1 = x
            else:
                x0 = x
        i += 1


# 求解f(x) = x^2 - 5 = 0
print solve(lambda x: x ** 2 - 5, 5, 0, 1e-8)

# 求解f(x) = x^2 - 2 = 0
print solve(lambda x: x ** 2 - 2, 0, 2, 1e-8)