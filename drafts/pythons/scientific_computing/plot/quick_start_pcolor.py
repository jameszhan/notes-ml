# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(5)
# y = np.arange(3)
# X, Y = np.meshgrid(x, y)
# print("X = {0}\nY = {1}".format(X, Y))
#
# C = np.random.randn(len(x), len(y))
# print("C = {0}".format(C))
#
# plt.subplot(2, 2, 1)
# plt.pcolor(X, Y, C.T)
#
# plt.subplot(2, 2, 3)
# plt.pcolormesh(X, Y, C.T)
#
# x = np.arange(-0.5, 5.5, 1, np.float)
# y = np.arange(-0.5, 3.5, 1, np.float)
#
# X, Y = np.meshgrid(x, y)
# print("x = {0}\ny = {1}".format(x, y))
# print("X = {0}\nY = {1}".format(X, Y))
# print("C = {0}".format(C))
# plt.subplot(2, 2, 2)
# plt.pcolormesh(X, Y, C.T)
#
# x = np.arange(0, 6, 1, np.float)
# y = np.arange(0, 4, 1, np.float)
# X, Y = np.meshgrid(x, y)
# print("x = {0}\ny = {1}".format(x, y))
# print("X = {0}\nY = {1}".format(X, Y))
# print("C = {0}".format(C))
# plt.subplot(2, 2, 4)
# plt.pcolormesh(X, Y, C.T)
#
# plt.show()

x = np.arange(5)
y = np.arange(3)
C = np.random.randn(len(x), len(y))

plt.subplot(2, 2, 1)
plt.pcolor(x, y, C.T)

plt.subplot(2, 2, 3)
plt.pcolormesh(x, y, C.T)

x = np.arange(-0.5, 5.5, 1, np.float)
y = np.arange(-0.5, 3.5, 1, np.float)
plt.subplot(2, 2, 2)
plt.pcolormesh(x, y, C.T)

x = np.arange(0, 6, 1, np.float)
y = np.arange(0, 4, 1, np.float)
plt.subplot(2, 2, 4)
plt.pcolormesh(x, y, C.T)

plt.show()


