# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


for x, y in [(i, sigmoid(i)) for i in range(-30, 30)]:
    print('sigmod({0}):\t{1}'.format(x, y))


x = np.linspace(-10, 10, 1000)
plt.plot(x, [sigmoid(v) for v in x], 'r:')
plt.grid(True)
plt.show()