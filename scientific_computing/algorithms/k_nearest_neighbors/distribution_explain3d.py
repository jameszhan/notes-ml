# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

# plt.figure()
ax = plt.subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

count = 100
sigma1, sigma2 = 30, 2.5
x1 = np.random.normal(50, sigma1, count)
y1 = np.random.normal(5, sigma2, count)
z1 = np.random.normal(10, 1, count)

x2 = np.random.normal(30, sigma1, count)
y2 = np.random.normal(4, sigma2, count)
z2 = np.random.normal(20, 1, count)

x3 = np.random.normal(45, sigma1, count)
y3 = np.random.normal(2.5, sigma2, count)
z3 = np.random.normal(30, 1, count)

ax.scatter(x1, y1, z1, c='b', marker='s', s=30, alpha=0.7)
ax.scatter(x2, y2, z2, c='r', marker='^', s=30, alpha=0.7)
ax.scatter(x3, y3, z3, c='g', s=30, alpha=0.7)
ax.scatter([50, 30, 45], [5, 4, 2.5], [10, 20, 30], c='k', marker='*', s=500, alpha=1.0)

plt.show()

