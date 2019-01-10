# -*- coding: utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


figure = plt.figure()
ax = Axes3D(figure)

x1 = np.linspace(0, 10, 100)
x2 = np.linspace(0, 10, 100)


ax.plot(x1, x2, 1 + 2 * x1 + 3 * x2, 'b--')

_x2 = x1 * 0
ax.plot(x1, _x2, 1 + 2 * x1 + 3 * _x2, 'r--')

_x1 = x1 * 0
ax.plot(_x1, x2, 1 + 2 * _x1 + 3 * x2, 'r--')

x1, x2 = np.meshgrid(x1, x2)
ax.plot_surface(x1, x2, 1 + 2 * x1 + 3 * x2, cmap=plt.cm.winter)
ax.plot_surface(x1, x2, x1 - x2)
ax.plot_surface(x1, x2, x1 + x2)

_x1 = np.linspace(0, 10, 10)
_x2 = np.linspace(0, 10, 10)

ax.scatter(_x1, _x2, 1 + 2 * _x1 + 3 * _x2, c='k', marker='o')

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')

plt.show()