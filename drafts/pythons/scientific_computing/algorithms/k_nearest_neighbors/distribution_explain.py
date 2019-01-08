# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 15
fig_size[1] = 10
plt.axis((10, 70, 1, 7))


def subgraph(sigma1, sigma2, index, count=100):
    x1 = np.random.normal(50, sigma1, count)
    y1 = np.random.normal(5, sigma2, count)

    x2 = np.random.normal(30, sigma1, count)
    y2 = np.random.normal(4, sigma2, count)

    x3 = np.random.normal(45, sigma1, count)
    y3 = np.random.normal(2.5, sigma2, count)

    plt.subplot(3, 2, index)
    plt.scatter(x1, y1, c='b', marker='s', s=30, alpha=0.7)
    plt.scatter(x2, y2, c='r', marker='^', s=30, alpha=0.7)
    plt.scatter(x3, y3, c='g', s=30, alpha=0.7)
    plt.scatter([50, 30, 45], [5, 4, 2.5], c='k', marker='*', s=100, alpha=1.0)


subgraph(2, 0.2, 1, 100)
subgraph(2, 0.2, 2, 500)
subgraph(6, 0.5, 3, 100)
subgraph(6, 0.5, 4, 500)
subgraph(30, 2.5, 5, 100)
subgraph(30, 2.5, 6, 500)

plt.show()

